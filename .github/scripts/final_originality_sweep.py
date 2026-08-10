from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

new_objs='''const objs=[
{n:"bowling ball",e:"🎳",m:4,u:"kg"},
{n:"sports equipment bag",e:"🎒",m:3,u:"kg"},
{n:"box of training cones",e:"📦",m:5,u:"kg"},
{n:"medicine ball",e:"🏐",m:2,u:"kg"},
{n:"tennis ball",e:"🎾",m:60,u:"g"},
{n:"skipping rope",e:"➰",m:250,u:"g"},
{n:"stopwatch",e:"⏱️",m:80,u:"g"},
{n:"training bib",e:"👕",m:180,u:"g"},
{n:"beanbag",e:"🟦",m:120,u:"g"},
{n:"relay baton",e:"🏃",m:140,u:"g"}
];'''
s,n=re.subn(r'const objs=\[.*?\];',new_objs,s,count=1,flags=re.S)
if n!=1: raise SystemExit('object bank not replaced')

s=s.replace('Which is the most sensible mass for a travel bag?', 'Which is the most sensible mass for a bowling ball?')
s=s.replace('card({n:"travel bag",e:"🧳"},"Mass ?")', 'card({n:"bowling ball",e:"🎳"},"Mass ?")')
s=s.replace('sh(["2 kg","2 g","200 g","20 kg"]),a:"2 kg",x:"2 kg is a sensible estimate for a travel bag."', 'sh(["4 kg","4 g","400 g","40 kg"]),a:"4 kg",x:"4 kg is a sensible estimate for a bowling ball."')
s=s.replace('Which is the most sensible mass for a pear?', 'Which is the most sensible mass for a tennis ball?')
s=s.replace('card({n:"pear",e:"🍐"},"Mass ?")', 'card({n:"tennis ball",e:"🎾"},"Mass ?")')
s=s.replace('sh(["160 g","160 kg","16 kg","2 kg"]),a:"160 g",x:"160 g is a sensible estimate for a pear."', 'sh(["60 g","60 kg","600 g","6 kg"]),a:"60 g",x:"60 g is a sensible estimate for a tennis ball."')

p.write_text(s,encoding='utf-8')
