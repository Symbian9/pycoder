#随缘情恋
#供麦友学习之用
import appuifw
import inbox
i=inbox.Inbox()
m=i.sms_messages()
list=[]
for t in m:
 list.append(i.content(t))
index=appuifw.selection_list(choices=list,search_field=1)
if index!=-1:
 appuifw.note(list[index])
