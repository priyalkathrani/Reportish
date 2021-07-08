from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
import matplotlib.pyplot as plt
from fpdf import FPDF

# Create your views here.
def hi(request):
    return render(request,'FORM/FORM.HTML')

def createPost(request):
    if request.method == 'POST':
        post=Post()
        post.gfname= request.POST.get('gfname')
        post.coname1= request.POST.get('coname1')
        post.coname2= request.POST.get('coname2')
        post.subname= request.POST.get('subname')
        post.dept= request.POST.get('dept')
        post.year= request.POST.get('year')
        post.date= request.POST.get('date')
        post.day = request.POST.get('day')
        post.s_time= request.POST.get('s_time')
        post.e_time= request.POST.get('e_time')
        post.venue= request.POST.get('venue')
        post.topic1 = request.POST.get('topic1')
        post.topic2 = request.POST.get('topic2')
        post.topic3 = request.POST.get('topic3')
        post.topic4 = request.POST.get('topic4')
        post.image1= request.POST.get('image1')
        post.tf= request.POST.get('tf')
        post.c_agree= request.POST.get('c_agree')
        post.agree= request.POST.get('agree')
        post.disagree= request.POST.get('disagree')
        post.c_disagree= request.POST.get('c_disagree')
        post.comments= request.POST.get('comments')
        post.save()

        path = '/Users/Vishv/Desktop/'
        
        f_name = post.gfname
        subject = post.subname
        topic1 = post.topic1
        topic2 = post.topic2
        topic3 = post.topic3
        topic4 = post.topic4
        dept = post.dept
        date = post.date
        day = post.day
        s_time = post.s_time
        e_time = post.e_time
        venue = post.venue
        year = post.year
        faculty = post.coname1
        t_feedback = post.tf
        c_agree = post.c_agree
        agree = post.agree
        disagree = post.disagree
        c_disagree = post.c_disagree
        comments = post.comments

        labels = ["Completely Agree", "Agree", "Disagree", "Completely Disagree"]
        values = [c_agree, agree, disagree, c_disagree]


        plt.pie(values, labels=labels, autopct="%.1f%%")
        plt.savefig(path + f_name + '.png')

        pdf = FPDF()
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.set_font('Times', 'B', 14)
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(20)
        pdf.image(path + 'charudep.png', x = None, y = None, w = 172, h = 20)
        pdf.cell(50, 5, " ", 0, 2, 'C')
    
        pdf.ln()
        pdf.cell(75)
        pdf.cell(40, 10, "CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY", 0, 2, 'C')
        pdf.cell(9)
        pdf.set_font_size(12)
        pdf.cell(20, 10, "DEVANG PATEL INSTITUTE OF ADVANCE TECHNOLOGY AND RESEARCH", 0, 2, 'C')
        pdf.ln()

        pdf.set_font_size(14)
        pdf.cell(75)
        pdf.cell(30, 10, "A Report", 0, 2, 'C')
        pdf.cell(1)
        pdf.cell(30, 10, "On", 0, 2, 'C')
        pdf.cell(1)
        pdf.cell(30, 10, "Expert Lecture of "+ subject, 0, 2, 'C')

        pdf.cell(70, 5, " ", 0, 2, 'C')

        pdf.set_font('Times', '', 12)
        pdf.cell(-62)
        pdf.cell(24, 10, 'Date: ' + date, 0, 2, 'C')
        pdf.cell(-1)
        pdf.cell(26, 10, 'Day: ' + day, 0, 2, 'C')
        pdf.cell(7)
        pdf.cell(18, 10, 'Time: ' + s_time + ' to ' + e_time, 0, 2, 'C')
        pdf.cell(2)
        pdf.cell(30, 10, 'Venue: ' + venue, 0, 2, 'C')
        pdf.cell(90, 10, " ", 0, 2, 'C')

        pdf.cell(95)
        pdf.cell(50, 50, faculty, 1, 2, 'C')
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()

        pdf.cell(9)
        pdf.image(path + 'charudep.png', x = None, y = None, w = 172, h = 20)

        pdf.cell(90, 10, " ", 0, 2, 'C')

        pdf.cell(1)
        pdf.multi_cell(170, 5, 'Devang Patel Institute of Advance Technology and Research (DEPSTAR) always inspire students for the overall development in academics and co-curricular activities. The institution is devoted to intellectually vibrant atmosphere of research and imparts education in learning of sciences. The main objective of this expert lecture was to introduce the learners about the ' + subject + '. In this Expert Lecture, many topics were discussed by resource person. Doubts of students were even solved and question answer session was conducted. The audience were ' + year + ' students of DEPSTAR of ' + dept + ' branches. ' + venue +' was booked for conducting the expert lecture. There was no registration fees for attending the expert lecture. The resource person of the workshop was ' + f_name + '.', 0, 'J')

        pdf.cell(50, 7, " ", 0, 2, 'C')
        pdf.cell(10)
        pdf.cell(60, 10, 'The topics covered by the resource person were:', 0, 2, 'J')
        pdf.cell(60, 10, '-> ' + topic1, 0, 2, 'J')
        pdf.cell(60, 10, '-> ' + topic2, 0, 2, 'J')
        pdf.cell(60, 10, '-> ' + topic3, 0, 2, 'J')
        pdf.cell(60, 10, '-> ' + topic4, 0, 2, 'J')
        pdf.ln()

        pdf.cell(10)
        pdf.multi_cell(170, 5, comments, 0, 'J')
        pdf.ln()
        
        pdf.ln()
        pdf.cell(10)
        pdf.multi_cell(170, 5, 'Feedback was taken from ' + t_feedback+ ' students at the end of workshop. Evaluation of Feedback is as per given below:', 0, 'J')
        pdf.ln()

        pdf.set_font('Times', 'B', 14)
        pdf.ln()
        pdf.cell(85)
        pdf.cell(20, 14, 'Evaluation of Feedback', 0, 2, 'C')
        pdf.set_font('Times', '', 12)
        pdf.cell(1)
        pdf.cell(20, 12, 'Person: ' + f_name, 0, 2, 'C')
        pdf.cell(1)
        pdf.cell(20, 12, 'Date: ' + date, 0, 2, 'C')
        pdf.cell(1)
        pdf.cell(20, 12, 'Time: ' + s_time + ' to ' + e_time, 0, 2, 'C')
        pdf.cell(-1)
        pdf.cell(20, 12, 'Venue: ' + venue, 0, 2, 'C')
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()

        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(10)
        pdf.image(path + 'charudep.png', x = None, y = None, w = 172, h = 20)
        pdf.cell(50, 7, " ", 0, 2, 'C')

        pdf.cell(30)
        pdf.image(path + f_name +'.png', x = None, y = None, w = 120, h = 90)
        pdf.ln()

        pdf.cell(18)
        pdf.cell(20, 12, 'Report Prepared By:', 0, 2, 'C')
        pdf.cell(-7)
        pdf.cell(30, 12, '' + faculty, 0, 2, 'C')
        
        pdf.cell(11)
        pdf.cell(20, 12, 'Devang Patel Institute Of', 0, 2, 'C')
        pdf.cell(1)
        pdf.cell(20, 12, 'Advance Technology And', 0, 2, 'C')
        pdf.cell(-3)
        pdf.cell(20, 12, 'Research (DEPSTAR)', 0, 2, 'C')

        pdf.output(path + f_name +'.pdf')
        return HttpResponse("<h1>Hello. Your PDF is downloaded on your Desktop!!!</h1>")