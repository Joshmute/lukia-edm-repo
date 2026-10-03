"""Reproducible synthetic assignment inputs (seed 40008). No instructor or real customer data."""
from pathlib import Path
import csv,json,random,calendar,hashlib
from datetime import date,timedelta
R=random.Random(40008); OUT=Path('data/simulation');OUT.mkdir(exist_ok=True)
def write(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# Scenario districts are fixed by the brief; the customer and store mix is not.
D=['Kampala','Kampala','Jinja','Mbarara','Kampala','Gulu','Jinja','Mbarara']
C=['Fresh Food','Dairy & Eggs','Personal Care','Cleaning','Drinks']
TYPO={'Fresh Food':'fresh fod','Dairy & Eggs':'diary & eggs','Personal Care':'personal-care','Cleaning':'cleanning','Drinks':'drinkz'}
TRUE_CUSTOMERS=4060;TRUE_PRODUCTS=1080;truth=[];dirty=[]
for i in range(TRUE_CUSTOMERS):
 r=dict(customer_id=f'LK-C{i+1:05}',name=f'Test Shopper {i+1:05}',phone=f'+2567{(i*7919+31)%10**8:08}',email=f'shopper.lk{i+1}@example.invalid',district=D[i%8],dob=f'{1965+i%41}-{1+i%12:02}-{1+i%27:02}',gender=['female','male','not_stated','female','male'][i%5],updated_at='2026-07-15' if i%6 else '2025-12-20')
 truth.append(r);d=dict(r)
 if i%13==0:d['phone']=''
 elif i%29==0:d['phone']='07-not-valid'
 elif i%5==0:d['phone']='0'+r['phone'][4:]
 elif i%5==1:d['phone']=r['phone'][1:]
 elif i%5==2:d['phone']='00'+r['phone'][1:]
 elif i%5==3:d['phone']='0'+r['phone'][4:7]+' '+r['phone'][7:]
 if i%13==0:d['email']=''
 elif i%31==0:d['email']=r['email'].replace('@','.at.')
 if i%37==0:d['district']='Kampla'
 elif i%41==0:d['district']='Unknown'
 elif i%4==0:d['district']=r['district'].upper()
 if i%43==0:d['name']=''
 elif i%6==0:d['name']=' '+r['name']+'   '
 if i%9==0:d['updated_at']='15/07/2026' if i%6 else '20/12/2025'
 elif i%7==0:d['updated_at']=r['updated_at'].replace('-','/')
 d['gender']={'male':'Male','female':'f','not_stated':''}[r['gender']]
 dirty.append(d)
# 940 repeated source records (18.8% of 5,000 rows) taken from across the file, not only its start.
dirty += [dict(dirty[(i*53)%TRUE_CUSTOMERS]) for i in range(940)]
R.shuffle(dirty)
write('SRG_Customers.csv',dirty);write('customer_truth.csv',truth)
write('verified_contact_updates.csv',[{**r,'verified_at':'2026-07-28','provenance':'SIMULATED call-centre confirmation'} for i,r in enumerate(truth) if i%13==0 or i%29==0 or i%31==0 or i%37==0 or i%41==0 or i%43==0])
products=[];pdirty=[];UNITS=['kg','l','each','g','each']
for i in range(TRUE_PRODUCTS):
 r=dict(sku=f'LK-P{i+1:04}',name=f'Catalogue Item {i+1:04}',unit=UNITS[i%5],category=C[(i*3)%5],updated_at='2026-07-01' if i%10 else '2026-02-14');products.append(r);d=dict(r)
 if i%4:d['unit']={'kg':['KGS','Kilograms'][i%2],'l':'liters','each':'pcs','g':'grams'}[r['unit']]
 if i%6==0:d['category']=TYPO[r['category']]
 elif i%5==0:d['category']=r['category'].lower()
 if i%8==0:d['sku']=r['sku'].lower()
 pdirty.append(d)
pdirty += [dict(pdirty[(i*17)%TRUE_PRODUCTS]) for i in range(120)]
R.shuffle(pdirty)
write('SRG_Products.csv',pdirty);write('product_truth.csv',products)
# 23 stores per the brief, unevenly spread: Kampala 9, Jinja 5, Mbarara 5, Gulu 4.
layout=[('Kampala',['Ntinda','Kansanga','Wandegeya','Nakawa','Kireka','Bukoto','Kabalagala','Nateete','Kawempe']),('Jinja',['Main Street','Walukuba','Bugembe','Mpumudde','Masese']),('Mbarara',['High Street','Kakoba','Ruharo','Nyamitanga','Kamukuzi']),('Gulu',['Layibi','Pece','Bardege','Laroo'])]
stores=[];n=0
for district,names in layout:
 for name in names:n+=1;stores.append(dict(store_id=f'LK-S{n:02}',name=f'{name} Branch',district=district))
write('SRG_Stores.csv',stores)
write('SRG_Suppliers.csv',[dict(supplier_id=f'LK-V{i+1:03}',name=f'Sample Vendor {i+1:03}',email=f'vendor.lk{i+1}@example.invalid',country=['Uganda','Uganda','Kenya','Uganda','Tanzania'][i%5]) for i in range(85)])
write('SRG_Loyalty.csv',[dict(account_id=f'LK-L{i+1:05}',customer_id=r['customer_id'],opening_points=(i*37)%500,marketing_consent=i%5!=0,consent_source='SIMULATED app enrolment',consent_at='2026-01-10') for i,r in enumerate(truth)])
SEG=['Budget','Family','Convenience','Loyal Plus']
write('SRG_CRM.csv',[dict(customer_id=r['customer_id'],segment=SEG[(i*7)%4],marketing_consent=i%5!=0,preference_updated_at='2026-07-15') for i,r in enumerate(truth)])
write('SRG_HR.csv',[dict(employee_id=f'LK-E{i+1:03}',name=f'Sample Staff {i+1:03}',salary_ugx=650000+i*31000,bank_account=f'FAKE-ACCT-{i+1:03}',national_id=f'FAKE-NIN-{i+1:03}',health_note='SIMULATED medical leave note',next_of_kin_phone=f'FAKE-KIN-{i+1:03}') for i in range(52)])
BASE={'Fresh Food':1500,'Dairy & Eggs':2500,'Personal Care':4000,'Cleaning':3500,'Drinks':1200}
sales=[];payments=[];canonical=[];counts=[8800,9400,10600,9700,10300,11200];index=0
for month,count in zip(range(2,8),counts):
 # Customers join in waves (Feb, Apr, Jun); one in six of the first wave stops buying after April.
 pool=[r for i,r in enumerate(truth) if (i<2900 or (i<3500 and month>=4) or month>=6) and not (i<2900 and i%6==0 and month>4)]
 for k in range(count):
  index+=1;source=R.choices(['pos','ecommerce','loyalty_app'],[50,30,20])[0];customer=R.choice(pool);product=products[R.randrange(TRUE_PRODUCTS)];store=R.choices(stores,[3 if s['district']=='Kampala' else 2 if s['district']=='Jinja' else 1.5 for s in stores])[0]
  day=date(2026,month,1)+timedelta(days=R.randrange(calendar.monthrange(2026,month)[1]))
  qty=-R.randint(1,2) if R.random()<0.03 else R.choices([1,2,3,4,6],[40,25,15,12,8])[0]
  price=BASE[product['category']]+(int(product['sku'][-4:])*37)%40*150
  currency='UGX' if index%60 else ('RWF' if index%120==0 else 'KES')
  if currency=='KES':price=max(40,price//28)
  if currency=='RWF':price=price*10//27
  provider=R.choices(['cash','MTN','Airtel'],[80,12,8])[0] if source=='pos' else R.choices(['MTN','Airtel'],[58,42])[0];ref='' if provider=='cash' or index%89==0 else f'LK-TXN-{index:06}'
  native_date=day.strftime('%d/%m/%Y') if source=='pos' else day.isoformat() if source=='ecommerce' else day.strftime('%d-%b-%Y')
  notation=f'{currency} {price:,}' if source=='pos' else str(price) if source=='ecommerce' else f'{price:,.2f}'
  row=dict(source=source,order_id=f'LK-O{index:06}',line_no=1,order_date=native_date,customer_id='' if index%29==0 else customer['customer_id'],sku=product['sku'].lower() if source=='pos' else product['sku'],store_id=store['store_id'],quantity=qty,unit_price=notation,currency=currency,payment_ref=ref)
  sales.append(row);canonical.append({**row,'order_date':day.isoformat(),'sku':product['sku'],'unit_price':price})
  if provider!='cash':payments.append(dict(provider=provider,provider_ref=ref or f'LK-NOREF-{index}',order_id=row['order_id'],store_id=store['store_id'],occurred_at=day.isoformat(),amount=qty*price,currency=currency,status='reversed' if qty<0 else 'completed'))
write('SRG_Sales.csv',sales);write('sales_truth.csv',canonical);write('SRG_MobileMoney.csv',payments)
inventory=[]
for store in stores:
 for product in products[:150]:
  book=R.randint(0,90);physical=max(0,book+R.choice([0,0,-1,1,-3,-4,0,2]))
  inventory.append(dict(snapshot_at='2026-07-31T19:30:00Z',store_id=store['store_id'],sku=product['sku'],on_hand=book,physical_count=physical,unit=product['unit'],source='SIMULATED Odoo'))
write('SRG_Inventory.csv',inventory)
events=[dict(event_id=f'LK-F{i+1:05}',store_id=stores[i%23]['store_id'],device_id=f'LK-D{i%23:02}',event_time_utc=f'2026-07-29T{7+i//70%12:02}:{i%60:02}:{(i*13)%60:02}Z',count_delta=1 if i%9 else -1,sequence=i,schema_version=2) for i in range(840)]
events+=[events[i] for i in (3,77,150,301,450,612,799)];(OUT/'footfall_stream_sample.json').write_text(json.dumps(events,indent=2))
(OUT/'etl_error_log.txt').write_text('SIMULATED FAILURE FIXTURE - not an instructor log\n2026-07-30T01:14:07Z ERROR batch=LK-117 source=pos row=2 date=14/02/2026 conversion failed: ISO date expected\n2026-07-30T01:14:08Z ERROR batch=LK-117 row=9 sku=lk-p0008 lookup failed: case-sensitive dictionary\n2026-07-30T01:16:41Z ERROR retry=1 batch=LK-117 duplicate business key source/order/line; previous rows were committed\n')
manifest={'classification':'SYNTHETIC ASSIGNMENT SIMULATION - not actual SRG observations','seed':40008,'counts':{'customer_rows':len(dirty),'distinct_customer_ids':TRUE_CUSTOMERS,'product_rows':len(pdirty),'distinct_skus':TRUE_PRODUCTS,'sales_rows':len(sales)},'period':'2026-02-01 to 2026-07-31','generated_by':'scripts/generate_simulation.py','files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir()) if p.suffix in ('.csv','.json','.txt') and p.name!='manifest.json'}}
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest['counts']))
