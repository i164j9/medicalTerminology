suf = open("suffix.json",'a')
pre = open("prefix.json",'a')
rot = open("roots.json",'a')

user_entry=''

while user_entry != 'quit':
    user_entry = input("enter term: ")
    definition = input("enter definition: ")
    print(user_entry[-2]+user_entry[-1])

    if user_entry[-1] == "-":
        #pre.write("{\"prefix\":\"user_entry\",\"meaning\":\"definition\"},")
        line_pre ="\n\t\t{\n\t\t\t\"prefix\":\""
        line_mid="\",\n\t\t\t\"meaning\":\""
        line_post =  "\"\n\t\t},"
        line = line_pre + user_entry + line_mid + definition + line_post
        print("\n\t"+line)
        pre.write("\n\t"+line)
        pre.flush()
    elif user_entry[-2]+user_entry[-1] == '/o' or user_entry[-2]+user_entry[-1] == '/i' or user_entry[-2]+user_entry[-1] == '/e':
        line_pre = "\n\t\t{\n\t\t\t\"root\":\""
        line_mid = "\",\n\t\t\t\"meaning\":\""
        line_post = "\"\n\t\t},"
        line = line_pre + user_entry + line_mid + definition + line_post
        print("\n\t"+line)
        rot.write("\n\t"+line)
        rot.flush()
    elif user_entry[0] == '-':
        line_pre = "\n\t\t{\n\t\t\t\"suffix\":\""
        line_mid = "\",\n\t\t\t\"meaning\":\""
        line_post = "\"\n\t\t},"
        line = line_pre + user_entry + line_mid + definition + line_post
        print(line)
        suf.write(line)
        suf.flush()
    else:
        print("re-enter your term and definition")

pre.close()
rot.close()
suf.close()