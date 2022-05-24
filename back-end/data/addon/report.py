import os
import sys
company = sys.argv[1]
email = sys.argv[2]
cmd = """cat  ~/recon/we-hack/"""+company + """/gout.txt | grep -w 'low\|medium\|high\|critical' |  awk '{print "<tr><td>"$1"</td><td id=rep>"$2"</td><td>"$3"</td></tr>"}' >> ~/recon/we-hack/"""+company +"""/report.html"""
#cmd = """cat  ~/recon/Webintellect/"""+company + """/out.txt|  awk '{print "<tr><td>"$3"</td><td>"$5"</td><td>"$6"</td></tr>"}' >> ~/Desktop/report.html"""
os.system("cat ~/tools/we-hack/back-end/data/report/header.txt >> ~/recon/we-hack/"+company +"/report.html")
os.system("echo "+company+ ">> ~/recon/we-hack/"+company +"/report.html")
os.system("cat ~/tools/we-hack/back-end/data/report/mid.txt >> ~/recon/we-hack/"+company +"/report.html")
os.system(cmd)
os.system("cat ~/tools/we-hack/back-end/data/report/fotter.txt >> ~/recon/we-hack/"+company +"/report.html")

#os.system("python3 ~/tools/we-hack/back-end/data/addon/mail.py "+company+" "+email)
