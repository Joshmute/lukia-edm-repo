"""Generate editable draw.io files and SVG/PNG figures from the same graph."""
from pathlib import Path
import xml.etree.ElementTree as ET
import html,textwrap,math
import pymupdf
OUT=Path('diagrams');OUT.mkdir(exist_ok=True)

def graph(name,title,nodes,edges,w=1100,h=730,er=False):
    # node: id, label, x,y,width,height. edge: from,to,label,start,end.
    mx=ET.Element('mxfile',host='app.diagrams.net');d=ET.SubElement(mx,'diagram',name=title,id=name)
    model=ET.SubElement(d,'mxGraphModel',page='1',pageWidth=str(w),pageHeight=str(h));root=ET.SubElement(model,'root')
    ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="#ffffff"/><text x="25" y="35" font-family="Times New Roman" font-size="24" font-weight="bold" fill="#000000">{html.escape(title)}</text>']
    lookup={n[0]:n for n in nodes}
    for k,(a,b,label,*markers) in enumerate(edges):
        start,end=(markers+['',''])[:2]
        na,nb=lookup[a],lookup[b]
        ax,ay=na[2]+na[4]/2,na[3]+na[5]/2;bx,by=nb[2]+nb[4]/2,nb[3]+nb[5]/2
        dx,dy=bx-ax,by-ay
        def boundary(n,cx,cy,vx,vy):
            ratios=[]
            if vx:ratios.append(n[4]/2/abs(vx))
            if vy:ratios.append(n[5]/2/abs(vy))
            t=min(ratios);return cx+vx*t,cy+vy*t
        x1,y1=boundary(na,ax,ay,dx,dy);x2,y2=boundary(nb,bx,by,-dx,-dy)
        route=None
        if (a,b)==('store','order'):
            x1,y1=na[2],ay;x2,y2=nb[2],by
            route=[(x1,y1),(na[2]-45,y1),(na[2]-45,y2),(x2,y2)]
        elif name=='etl' and (a,b)==('c','q'):
            x1,y1=na[2]+na[4],ay;x2,y2=nb[2]+nb[4],by
            route=[(x1,y1),(1090,y1),(1090,y2),(x2,y2)]
        path='M'+ ' L'.join(f'{x},{y}' for x,y in (route or [(x1,y1),(x2,y2)]))
        svg.append(f'<path d="{path}" stroke="#000000" stroke-width="2" fill="none"/>')
        def marker(x,y,tx,ty,kind):
            length=math.hypot(tx,ty);ux,uy=tx/length,ty/length;vx,vy=-uy,ux
            def line(a,b,c,d):svg.append(f'<path d="M{a},{b} L{c},{d}" stroke="#000000" stroke-width="2"/>')
            if 'many' in kind:
                for s in (-8,0,8):line(x+ux*16,y+uy*16,x+vx*s,y+vy*s)
            if 'one' in kind:
                for t in (7,13):line(x+ux*t+vx*7,y+uy*t+vy*7,x+ux*t-vx*7,y+uy*t-vy*7)
            if 'zero' in kind:
                svg.append(f'<circle cx="{x+ux*24}" cy="{y+uy*24}" r="5" fill="#ffffff" stroke="#000000" stroke-width="2"/>')
            if not kind:
                line(x,y,x+ux*12+vx*5,y+uy*12+vy*5);line(x,y,x+ux*12-vx*5,y+uy*12-vy*5)
        if er:
            if route: marker(x1,y1,route[1][0]-x1,route[1][1]-y1,start);marker(x2,y2,route[-2][0]-x2,route[-2][1]-y2,end)
            else: marker(x1,y1,dx,dy,start);marker(x2,y2,-dx,-dy,end)
        else:
            marker(x2,y2,-dx,-dy,'')
            if name=='mdm-flows': marker(x1,y1,dx,dy,'')
        if label:
            tx=(x1+x2)/2;ty=(y1+y2)/2-8
            svg.append(f'<rect x="{tx-len(label)*4.2}" y="{ty-14}" width="{len(label)*8.4}" height="20" fill="#ffffff"/><text x="{tx}" y="{ty}" text-anchor="middle" font-family="Times New Roman" font-size="14" fill="#000000">{html.escape(label)}</text>')
        def arrow(k):return {'one':'ERmandOne','zero_one':'ERzeroToOne','many':'ERmany','zero_many':'ERzeroToMany'}.get(k,'block')
        style=f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow={arrow(end) if er else "block"};startArrow={arrow(start) if er else ("block" if name=="mdm-flows" else "none")};fontSize=14;'
        c=ET.SubElement(root,'mxCell',id=f'e{k}',value=label,style=style,edge='1',parent='1',source=a,target=b);ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
    for id,label,x,y,nw,nh in nodes:
        svg.append(f'<rect x="{x}" y="{y}" width="{nw}" height="{nh}" rx="8" fill="white" stroke="#000000" stroke-width="2"/>')
        lines=[]
        for part in label.split('\n'):lines.extend(textwrap.wrap(part,width=max(10,int(nw/9.3))) or [''])
        for k,line in enumerate(lines):svg.append(f'<text x="{x+12}" y="{y+25+k*22}" font-family="Times New Roman" font-size="{17 if k else 18}" font-weight="{"bold" if k==0 else "normal"}" fill="#000000">{html.escape(line)}</text>')
        c=ET.SubElement(root,'mxCell',id=id,value=html.escape(label).replace('\n','&lt;br&gt;'),style='rounded=1;whiteSpace=wrap;html=0;fillColor=#ffffff;strokeColor=#000000;fontSize=17;',vertex='1',parent='1')
        c.set('value',label)
        ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(nw),height=str(nh),attrib={'as':'geometry'})
    svg.append('</svg>');data=''.join(svg).encode();(OUT/f'{name}.svg').write_bytes(data)
    ET.ElementTree(mx).write(OUT/f'{name}.drawio',encoding='utf-8',xml_declaration=True)
    doc=pymupdf.open(stream=data,filetype='svg');doc[0].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(OUT/f'{name}.png')

graph('lifecycle','Customer lifecycle: responsibility at each hand-off',[
('create','CREATE\nPOS / app / checkout\nCashier + customer\nRisk: duplicate signup',30,80,310,160),
('store','STORE\nLocal DB + shared hub\nIT manager\nRisk: exposed export',395,80,310,160),
('use','USE\nLoyalty / CRM / BI\nCustomer owner + CFO\nRisk: wrong identity',760,80,310,160),
('share','SHARE\nPartners / processors\nDPO + procurement\nRisk: excess disclosure',760,390,310,160),
('archive','ARCHIVE\nRestricted backups\nIT + record owner\nRisk: indefinite copies',395,390,310,160),
('delete','DELETE\nSources + hub + partners\nDPO + IT\nRisk: restore resurrects',30,390,310,160)],
[('create','store','validate'),('store','use','authorise'),('use','share','minimise'),('share','archive','schedule'),('archive','delete','expire')],h=610)

nodes=[('customer','Customer',40,100,240,90),('loyalty','LoyaltyAccount',40,390,240,90),('order','Order',430,100,240,90),('line','OrderLine',810,100,240,90),('payment','Payment',430,390,240,90),('store','Store',430,620,240,90),('product','Product',810,390,240,90),('supplier','Supplier',810,620,240,90)]
edges=[('customer','order','places','zero_one','zero_many'),('customer','loyalty','holds','one','zero_one'),('order','line','contains','one','many'),('order','payment','settles','one','zero_many'),('store','order','records','one','zero_many'),('product','line','sold as','one','zero_many'),('product','supplier','supplied by','zero_many','zero_many')]
graph('conceptual-er','Conceptual ER model | O optional, bar one, fork many',nodes,edges,h=770,er=True)

nodes=[('customer','Customer\nPK customer_id\nname, phone, email',25,80,300,135),('loyalty','LoyaltyAccount\nPK account_id\nFK customer_id UNIQUE\npoints_balance',25,360,300,150),('order','Order\nPK order_id\nFK customer_id nullable\nFK store_id\nordered_at, currency',400,80,300,175),('line','OrderLine\nPK/FK order_id\nPK line_no\nFK product_id\nquantity, unit_price',775,80,300,175),('payment','Payment\nPK payment_id\nFK order_id\nprovider, ref, amount',400,365,300,150),('store','Store\nPK store_id\nname, district',400,630,300,115),('product','Product\nPK product_id\nname, category, unit',775,365,300,135),('bridge','ProductSupplier\nPK/FK product_id\nPK/FK supplier_id\nsupplier_sku',775,630,300,150),('supplier','Supplier\nPK supplier_id\nname',775,895,300,110)]
edges=[('customer','order','','zero_one','zero_many'),('customer','loyalty','','one','zero_one'),('order','line','','one','many'),('order','payment','','one','zero_many'),('store','order','','one','zero_many'),('product','line','','one','zero_many'),('product','bridge','','one','zero_many'),('supplier','bridge','','one','zero_many')]
graph('logical-er','Logical ER model | keys and minimum/maximum cardinality',nodes,edges,h=1040,er=True)

graph('warehouse','Shared dimensions, separate fact grains',[
('sources','FIVE SOURCE FAMILIES\nPOS + e-commerce\nLoyalty app + CRM\nOdoo inventory',20,80,300,180),('hub','RESTRICTED HUB\nContracts + crosswalks\nQuality + consent\nReconciliation',400,80,300,180),('dims','CONFORMED DIMENSIONS\nDate + Customer\nProduct SCD2\nStore SCD2',790,80,290,180),
('sales','FactSales\nOne source order line\nSigned qty / amount\nDate, customer,\nproduct, store keys',30,430,300,175),('payment','FactPayment\nOne provider event\nStatus / amount\nStore + event time',400,430,300,175),('stock','FactInventorySnapshot\nProduct x store x time\nOn-hand quantity\nProduct + store keys',780,430,300,175)],
[('sources','hub','extract'),('hub','dims','resolve'),('dims','sales','version keys'),('dims','payment','store key'),('dims','stock','version keys'),('hub','sales','load'),('hub','payment','settlement feed')],h=650)

graph('etl','Batch ETL: commit and reconcile before advancing the watermark',[
('a','1. EXTRACT\nOutbox / API / CSV\nCount + checksum',20,80,300,130),('b','2. INTAKE\nImmutable raw copy\nRestricted access',400,80,300,130),('c','3. VALIDATE\nTypes / formats\nReference lookups',780,80,300,130),('d','4. DIMENSIONS\nReviewed crosswalks\nSCD2 at event time',780,385,300,130),('e','5. FACTS\nIdempotent keys\nSingle transaction',400,385,300,130),('f','6. CERTIFY\nTotals + exceptions\nCommit -> watermark',20,385,300,130),('q','QUARANTINE\nReason + owner + replay\nRetain source evidence',780,625,300,110)],
[('a','b','manifest'),('b','c','schema check'),('c','d','accepted'),('d','e','keys'),('e','f','reconcile'),('c','q','')],h=780)

graph('streaming','Selective streaming | footfall is not stock or payment evidence',[
('edge','EDGE / SOURCE EVENTS\nFootfall counts\nStock movements\nProvider payment events',25,85,300,170),('broker','DURABLE BROKER\nAt-least-once delivery\nRetry + dead-letter\nNo personal footfall IDs',400,85,300,170),('consumer','CONSUMERS\nDeduplicate event IDs\nEvent-time windows\nLate-event handling',775,85,300,170),('foot','FOOTFALL VIEW\nFive-minute counts\nDevice health\nNo person tracking',25,420,300,150),('stock','STOCK VIEW\nMovement balances\nLast-seen freshness\nDaily reconciliation',400,420,300,150),('fraud','PAYMENT ALERTS\nDuplicate / reversal\nOrder + settlement join\nHuman review',775,420,300,150)],
[('edge','broker','persist'),('broker','consumer','consume'),('consumer','foot','counts'),('consumer','stock','movements'),('consumer','fraud','payments')],h=620)

graph('lineage','Monthly active customers | every hop has a defined rule',[
('raw','RAW INPUT\nsource_customer_id\norder_time + quantity\nSource manifest/hash',20,85,300,165),('clean','STANDARDISE\nApproved date parser\nKampala business date\nPreserve return sign',400,85,300,165),('resolve','RESOLVE IDENTITY\nApproved crosswalk\nUnresolved -> exception\nAnonymous stays null',780,85,300,165),('facts','WAREHOUSE FACT\nSource/order/line key\nHistorical dimension keys\nReconcile before certify',780,405,300,165),('metric','METRIC\nquantity > 0\nDistinct customer_key\nGroup by month',400,405,300,165),('board','BOARD VISUAL\nMonth/channel filters\nFreshness and coverage\nDo not add distincts',20,405,300,165)],
[('raw','clean','parse'),('clean','resolve','match'),('resolve','facts','load'),('facts','metric','filter'),('metric','board','render')],h=620)
# Fishbone rendered as explicit causes-to-effect graph, with central spine and labelled ribs.
graph('fishbone','Stock variance hypotheses | S systemic, P point of entry',[
('p','PEOPLE\nP: rushed receiving\nP: return miscoding',20,80,270,130),('process','PROCESS\nS: unmatched transfers\nS: no count cutoff',400,80,270,130),('system','SYSTEMS\nS: late offline sync\nS: missing retries',780,80,290,130),('measure','MEASUREMENT\nS: mixed snapshot times\nP: physical miscount',20,430,270,130),('master','MASTER DATA\nS: conflicting SKU map\nP: wrong pack units',400,430,270,130),('loss','CONTROL ENVIRONMENT\nS: weak approvals\nP: unrecorded shrinkage',780,430,290,130),('effect','REPORTED 8.4% VARIANCE\nCause and denominator unverified',365,285,420,90)],
[('p','effect',''),('process','effect',''),('system','effect',''),('measure','effect',''),('master','effect',''),('loss','effect','')],h=610)

# Replace the stock cause graph with a conventional fishbone (Ishikawa) layout.
def fishbone():
    w,h=1100,540
    mx=ET.Element('mxfile',host='app.diagrams.net');d=ET.SubElement(mx,'diagram',name='Stock variance fishbone',id='fishbone')
    root=ET.SubElement(ET.SubElement(d,'mxGraphModel'),'root');ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"><rect width="100%" height="100%" fill="#ffffff"/><text x="25" y="35" font-family="Times New Roman" font-size="23" font-weight="bold" fill="#000000">Stock variance fishbone | S systemic, P point of entry</text>']
    def line(id,x1,y1,x2,y2):
        parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#000000" stroke-width="2.5" fill="none"/>')
        c=ET.SubElement(root,'mxCell',id=id,edge='1',parent='1',style='endArrow=none;strokeColor=#000000;strokeWidth=2;');g=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'});ET.SubElement(g,'mxPoint',x=str(x1),y=str(y1),attrib={'as':'sourcePoint'});ET.SubElement(g,'mxPoint',x=str(x2),y=str(y2),attrib={'as':'targetPoint'})
    def label(id,x,y,lines,width=250):
        for j,t in enumerate(lines):parts.append(f'<text x="{x}" y="{y+j*23}" font-family="Times New Roman" font-size="{18 if j==0 else 16}" font-weight="{"bold" if j==0 else "normal"}" fill="#000000">{html.escape(t)}</text>')
        c=ET.SubElement(root,'mxCell',id=id,value='\n'.join(lines),vertex='1',parent='1',style='text;html=0;whiteSpace=wrap;fontSize=17;align=left;');ET.SubElement(c,'mxGeometry',x=str(x),y=str(y-20),width=str(width),height=str(len(lines)*23+12),attrib={'as':'geometry'})
    line('spine',40,280,875,280)
    cats=[('PEOPLE','P: rushed receiving','P: return miscoding'),('PROCESS','S: unmatched transfers','S: no count cutoff'),('SYSTEMS','S: late offline sync','S: missing retries'),('MEASUREMENT','S: mixed snapshot times','P: physical miscount'),('MASTER DATA','S: conflicting SKU map','P: wrong pack units'),('CONTROL','S: weak approvals','P: unrecorded shrinkage')]
    for j,lines in enumerate(cats):
        col=j%3;x=50+col*275;top=j<3
        line(f'rib{j}',x+65,175 if top else 395,x+160,280)
        label(f't{j}',x,95 if top else 435,lines)
    parts.append('<rect x="875" y="225" width="205" height="110" rx="8" fill="#ffffff" stroke="#000000" stroke-width="2"/>')
    label('effect',890,250,['REPORTED 8.4%','STOCK VARIANCE','Cause unverified'],190)
    parts.append('</svg>');data=''.join(parts).encode();(OUT/'fishbone.svg').write_bytes(data);ET.ElementTree(mx).write(OUT/'fishbone.drawio',encoding='utf-8',xml_declaration=True)
    doc=pymupdf.open(stream=data,filetype='svg');doc[0].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(OUT/'fishbone.png')
fishbone()
graph('mdm-flows','Customer MDM: local creation and reviewed corrections',[
('pos','STORE POS\nOffline provisional ID\nDurable outbox\nApply mapping version',30,85,300,155),
('web','E-COMMERCE\nVerified contact update\nCheckout identity\nApply mapping version',770,85,300,155),
('hub','GOLDEN RECORD HUB\nSource crosswalk + review\nSurvivorship + consent\nReversible merge ledger',390,335,320,155),
('loyalty','LOYALTY\nAccount + points ledger\nVerified claims\nProtect balance history',30,575,300,155),
('crm','CRM\nPurpose-specific choices\nSuppression first\nApproved customer view',770,575,300,155)],
[('pos','hub','events / mappings'),('web','hub','updates / mappings'),('hub','loyalty','claims / identity'),('hub','crm','choices / identity')],h=790)

print('Built 9 editable draw.io diagrams and matching SVG/PNG figures')
