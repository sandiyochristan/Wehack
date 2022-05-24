import os
import sys
company = sys.argv[1]
email = sys.argv[2]

print ("company ==== "+company)

#sub =' python ~/tools/github-search/github-subdomains.py -t <your token> -d ~/recon/we-hack/'+company + '/raw.txt > ~/recon/we-hack/' + company + '/gout.txt  '
sub1 =' subfinder -dL ~/recon/we-hack/'+company + '/raw.txt -o ~/recon/we-hack/'+company + '/sout.txt '
sub2 = 'amass enum -passive -df ~/recon/we-hack/'+company + '/raw.txt -o ~/recon/we-hack/'+company + '/aout.txt'
sort =' cat ~/recon/we-hack/'+company + '/*.txt | sort -u >> ~/recon/we-hack/'+company + '/all.txt'
naabu = 'naabu -list ~/recon/we-hack/'+company + '/all.txt -o ~/recon/we-hack/'+company + '/nabu.txt'
liv = ' cat ~/recon/we-hack/'+company + '/nabu.txt |  httpx | tee -a ~/recon/we-hack/'+company + '/live.txt'
smug = 'cat ~/recon/we-hack/'+company + '/live.txt | python3 ~/tools/smuggler/smuggler.py --no-color | tee -a ~/recon/we-hack/'+company + '/smug.txt'
comb = 'cat ~/recon/we-hack/'+company + '/live.txt >> ~/recon/we-hack/'+company + '/nabu.txt'
scan = ' nuclei -list ~/recon/we-hack/'+company + '/nabu.txt -o ~/recon/we-hack/' + company + '/out.txt  '
rep = """cat ~/recon/we-hack/"""+company + """/out.txt| awk '{print $3 "   "$5 "   " $6}' >> ~/recon/we-hack/""" + company + "/gout.txt"

#os.system(sub)
os.system(sub1)
os.system(sub2)
print("sort")
os.system(sort)
os.system(naabu)
print("naabu done")
os.system(liv)
print("live done")
os.system(smug)
print("smug")
os.system(comb)
print("scan started")
os.system(scan)
os.system(rep)
os.system("python ~/tools/we-hack/back-end/data/addon/report.py " +company+ " " +email)



#cat bugs.txt| grep -w 'low\|medium\|high\|critical' | awk '{print "{BugName:"$3",Piority:"$5",Point:"$6"}"}' ----> create json data
#cat bugs.txt| grep -w 'low\|medium\|high\|critical' | awk '{print $3","$5","$6}'
