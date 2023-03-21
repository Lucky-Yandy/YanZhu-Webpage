import glob
all_content_files = glob.glob("content/*.html")

import os             

pages=[]

for item in all_content_files:
    
    file_name = os.path.basename(item)
    name_only, extension = os.path.splitext(file_name)
    #print(name_only)
    output_filename = 'docs/'+file_name
    pages.append({
       'filename':item,
        'filename_link':file_name,
        'title':name_only,
        'output': output_filename,
       }
       )


from jinja2 import Template

template_html= open('./templates/base.html').read() 

template=Template(template_html)



finished_page=''
def main():
    
     for page in pages:
          filename = page['filename'] 
          output = page['output'] 
          title =page['title']   
 
          context = { }
          context['title'] = title
          context['content'] = open(filename).read()
          context['pages'] = pages
          finished_page = template.render(context) 
          open(output, "w+").write(finished_page)
      

main()





