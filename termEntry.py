
suf = open("suffix.json",'a')
pre = open("prefix.json",'a')
rot = open("root.json",'a')

user_entry=''
definitions=[]
definition='1'

line_mid="\",\n\t\t\t\"meaning\":["
line_post =  "]\n\t\t},"

while user_entry != 'quit':
    user_entry = input("enter term: ")
    while definition != '':
        definition = input("enter definition: ")
        if definition != '':
            definitions.append(definition)
    print(definitions)
    counter = 0
    if user_entry[-1] == "-":
        line_pre ="\n\t\t{\n\t\t\t\"prefix\":\""
        line = line_pre + user_entry + line_mid
        if len(definitions) > 1:
            for d in definitions:
                if counter < len(definitions):
                    counter = counter + 1
                    line = line + "\"" + d + "\""
                    if counter < len(definitions):
                        line = line + ","
            line = line + line_post            
        else:
            line = line_pre + user_entry + line_mid + "\"" + definitions[0] +"\""+ line_post
        
        definitions.clear()
        print(line+"\n")
        pre.write(line)
        pre.flush()

    elif user_entry[-2]+user_entry[-1] == '/o' or user_entry[-2]+user_entry[-1] == '/i' or user_entry[-2]+user_entry[-1] == '/e':
        line_pre ="\n\t\t{\n\t\t\t\"root\":\""
        line = line_pre + user_entry + line_mid
        if len(definitions) > 1:
            for d in definitions:
                if counter < len(definitions):
                    counter = counter + 1
                    line = line + "\"" + d + "\""
                    if counter < len(definitions):
                        line = line + ","
        else:
            line = line_pre + user_entry + line_mid + "\"" + definition +"\""+ line_post
        line = line + line_post
        definitions.clear()
        print(line+"\n")
        rot.write(line)
        rot.flush()

    elif user_entry[0] == '-':
        line_pre ="\n\t\t{\n\t\t\t\"suffix\":\""
        line = line_pre + user_entry + line_mid
        if len(definitions) > 1:
            for d in definitions:
                if counter < len(definitions):
                    counter = counter + 1
                    line = line + "\"" + d + "\""
                    if counter < len(definitions):
                        line = line + ","
        else:
            line = line_pre + user_entry + line_mid + "\"" + definition +"\""+ line_post
        line = line + line_post
        definitions.clear()
        print(line+"\n")
        suf.write(line)
        suf.flush()

    else:
        print("re-enter your term and definition")

pre.close()
rot.close()
suf.close()