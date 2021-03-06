from tkinter import*
import visitor
import db

class viewPage:
    def __init__(self, name):
        self.name = name
        db.cursor.execute("SELECT reputation_score FROM users WHERE username = '%s'"%name)
        repScore = db.cursor.fetchone()[0]
        display_info = name + "\nReputation Score: " + str(repScore)

        # Get group id that user is in
        db.cursor.execute("SELECT group_id FROM group_membership WHERE username = '%s'"%name)
        #store all project id in array
        projList = []
        for row in db.cursor:
            projList.append(row)

        ##Store proj name in variable if exist
        try:
            db.cursor.execute("SELECT name FROM projects WHERE id = '%d'"%projList[0])
            proj1 = db.cursor.fetchone()[0]
        except:
            proj1 = "NULL"

        try:
            db.cursor.execute("SELECT name FROM projects WHERE id = '%d'"%projList[1])
            proj2 = db.cursor.fetchone()[0]
        except:
            proj2 = "NULL"
        try:
            db.cursor.execute("SELECT name FROM projects WHERE id = '%d'"%projList[2])
            proj3 = db.cursor.fetchone()[0]
        except:
            proj3 = "NULL"


        self.win = Tk()
        self.win.title("Top OU Profile")
        self.win.geometry('{}x{}'.format(1000, 600))
        self.canvas = Canvas(self.win, bg='white')
        self.profPic = PhotoImage(file = r"images/profile.png")
        self.icon = Label(self.canvas, image = self.profPic, bg = 'white')
        self.banner = Label(self.canvas, bg = "black", height = 4, width = 600)
        self.username = Label(self.canvas, text = display_info,
                        font="Arial 20 bold", bg = 'white')

        # place holder for top 3 projects
        self.project1 = Button(self.canvas, text=proj1, font='Arial 20 bold', bg='white', fg="black", width = 30, height = 2)
        self.project2 = Button(self.canvas, text=proj2, font='Arial 20 bold', bg='white', fg="black", width = 30, height = 2)
        self.project3 = Button(self.canvas, text=proj3, font='Arial 20 bold', bg='white', fg="black", width = 30, height = 2)
        self.back = PhotoImage(file = r"images/back.png")
        self.backButton = Button(self.canvas, image = self.back, command = self.visitor, bd = 0, bg = "black")

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.banner.place(x = 0, y= 0)
        self.icon.place(x = 50, y = 100)
        self.username.place(x = 50, y = 380)
        self.project1.place(x = 380, y = 150)
        self.project2.place(x = 380, y = 250)
        self.project3.place(x = 380, y = 350)
        self.backButton.place(x = 20, y = 20)

        self.win.mainloop()

    def visitor(self):
        self.win.destroy()
        back = visitor.VisitorPage()
        back.main()
