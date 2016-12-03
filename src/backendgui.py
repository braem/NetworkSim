import os
from Tkinter import *


from src import MessageSendingDemo


class Backgui:

    def __init__(self, master):
        #MessageSendingDemo.start_demo()

        self.frame = Frame(master)
        self.frame.pack()
        self.button = Button(self.frame,
                             text="QUIT", fg="red",
                             command=self.quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(self.frame,
                             text="Start",
                             command=self.startsimulation)
        self.slogan.pack(side=LEFT)
        self.slogan = Button(self.frame,
                             text="Stop",
                             command=self.pausesimulation)
        self.slogan.pack(side=LEFT)
        self.slogan = Button(self.frame,
                             text="Resume",
                             command=self.resumesimulation)

        self.slogan.pack(side=LEFT)
        self.slogan = Button(self.frame,
                             text="Add Node",
                             command=self.addnodes)
        self.slogan.pack(side=LEFT)

        self.add_node_text = StringVar()
        self.add_node_entry = Entry(self.frame, textvariable=self.add_node_text)
        self.add_node_entry.pack(side=LEFT)
        self.add_node_entry.insert(0,"connected Node ID")

        self.slogan = Button(self.frame,
                             text="Remove Node",
                             command=self.removenodes)
        self.slogan.pack(side=LEFT)

        self.rem_node_text = StringVar()
        self.rem_node_entry = Entry(self.frame, textvariable=self.rem_node_text)
        self.rem_node_entry.pack(side=LEFT)
        self.rem_node_entry.insert(0,"removed node_id")

        self.slogan = Button(self.frame,
                             text="Send Message",
                             command=self.sendmessage)
        self.slogan.pack(side=LEFT)

        self.src_id_text = StringVar()
        self.src_id_entry = Entry(self.frame, textvariable=self.src_id_text)
        self.src_id_entry.pack(side=LEFT)
        self.src_id_entry.insert(0,"From (ID)")

        self.dest_id_text = StringVar()
        self.dest_id_entry = Entry(self.frame, textvariable=self.dest_id_text)
        self.dest_id_entry.pack(side=LEFT)
        self.dest_id_entry.insert(0,"To (ID)")

        self.slogan = Button(self.frame,
                             text="Show Routing Table",
                             command=self.showroutingtable)
        self.slogan.pack(side=LEFT)

        self.rt_id_text = StringVar()
        self.rt_id_entry = Entry(self.frame, textvariable=self.rt_id_text)
        self.rt_id_entry.pack(side=LEFT)
        self.rt_id_entry.insert(0,"Node ID")

        self.slogan = Button(self.frame,
                             text="Show Network",
                             command=self.shownetwork)
        self.slogan.pack(side=LEFT)





    def quit(self):
        self.pausesimulation()
        self.frame.quit()


    def startsimulation(self):
        MessageSendingDemo.start_demo()


    def pausesimulation(self):
        MessageSendingDemo.stop_demo()

    def resumesimulation(self):
        MessageSendingDemo.resume_demo()

    def addnodes(self):
        text = self.add_node_text.get().split(',')
        node_id = text[0].strip()
        latency = text[1].strip()
        #try:
        MessageSendingDemo.add_node(int(text[0]), int(text[1]))
        #except: print Exception


    def removenodes(self):

        #try:
        MessageSendingDemo.remove_node((int(self.rem_node_text.get().strip())))
        #except: print "Node remove error"

    def showroutingtable(self):
        rt_id = int(self.rt_id_text.get().strip())
        table = MessageSendingDemo.get_routing_table(rt_id)

        table_window = Toplevel()
        label = Label(table_window, text=table, justify=LEFT)
        label.pack()

    def shownetwork(self):
        window = Toplevel()
        graph = MessageSendingDemo.get_graph()
        label1 = Label(window, text=graph, justify=LEFT)
        label1.pack(side=LEFT)
        table = MessageSendingDemo.get_packet_table()
        label2 = Label(window, text=table, justify = LEFT)
        label2.pack(side=LEFT)

    def sendmessage(self):
        to_id = int(self.dest_id_text.get().strip())
        from_id = int(self.src_id_text.get().strip())

        MessageSendingDemo.send_message(from_id, to_id, "Message")


# def show(self, obj, start=None):
#     if obj == start:
#         MessageSendingDemo.start_demo()
#
# a = raw_input("User Input")
# show(a, "start")


root = Tk() #It is just a holder
app = Backgui(root)
root.mainloop()  #important for closing th root=Tk()
