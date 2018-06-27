from wand.image import Image
from fpdf import FPDF

a4_h = 297
a4_w = 210
h = 165
w = 90
l=0;
# pdf_cover = FPDF("P","mm",(184,165))
# pdf_cover.add_page()
# pdf_cover.image("t-0.jpg",w=90,h=165,x=94,y=0)
# pdf_cover.output("cover.pdf","F")
pdf = FPDF("P","mm",(90,165))
# with Image(filename="p1.pdf",width=1800,height=3300,resolution=300) as img:
#      img.save(filename="p1/t.jpg")


for i in range(0,20):
    with Image(filename="p1/t-%d.jpg"%i,width=1800,height=3300) as image:
        image.crop(width=image.width,height=image.height//30*29,gravity='south')
        # image.resize(90*20,165*20)
        image.save(filename="1/after%d.jpg"%(i))
        pdf.add_page()
        pdf.image("1/after%d.jpg"%(i),w=90,h=165,x=0,y=0)

for i in range(0,20):
    with Image(filename="p2/t-%d.jpg"%i,width=1800,height=3300) as image:
        image.crop(width=image.width,height=image.height//30*29,gravity='south')
        # image.resize(90*20,165*20)
        image.save(filename="2/after%d.jpg"%(i))
        pdf.add_page()
        pdf.image("2/after%d.jpg"%(i),w=90,h=165,x=0,y=0)
for i in range(0,20):
    with Image(filename="p3/t-%d.jpg"%i,width=1800,height=3300) as image:
        image.crop(width=image.width,height=image.height//30*29,gravity='south')
        # image.resize(90*20,165*20)
        image.save(filename="3/after%d.jpg"%(i))
        pdf.add_page()
        pdf.image("3/after%d.jpg"%(i),w=90,h=165,x=0,y=0)
for i in range(0,26):
    with Image(filename="p4/t-%d.jpg"%i,width=1800,height=3300) as image:
        image.crop(width=image.width,height=image.height//30*29,gravity='south')
        # image.resize(90*20,165*20)
        image.save(filename="4/after%d.jpg"%(i))
        pdf.add_page()
        pdf.image("4/after%d.jpg"%(i),w=90,h=165,x=0,y=0)

pdf.output("output_noresize.pdf","F")

