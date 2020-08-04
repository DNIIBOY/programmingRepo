import keyboard
record = keyboard.record(until='esc+space+7')
save=open("hmm","w")
for i in record:
    save.write(str(i)+'\n')
save.close()
