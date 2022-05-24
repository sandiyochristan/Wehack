const express = require("express");
const app = express();
var bodyParser = require('body-parser');
const { spawn } = require("child_process");
const cors = require('cors');
app.use(cors());

app.use(express.json())
var urlencodedParser = bodyParser.urlencoded({ extended: false })
app.listen(443, () => {
    console.log("Application started and Listening on port 80");
});
app.get("/", (req, res) => {
    res.send({ title: 'helloworld' });
});

const email = "Sec@cappriciosec.com" ;

app.post('/createdb', urlencodedParser, function (req, res) {

    const { cname, subdomains, ip } = req.body;

    var subs = ''
    var date = new Date();
    const gtoken = req.body.cdomain;
    token = gtoken;
    sdate = date.toISOString().slice(0, 10);
    console.log(date.toISOString().slice(0, 10));
    const comapny_name = cname;
    const comapny_email = email;
    comapny = comapny_name
   
    aadom = [ip, ...subdomains]  // converting into array

    var exec = require('child_process').exec;
    var cmd = 'mkdir ~/recon/we-hack/' + comapny + ' &> /dev/null';
    exec(cmd, function (error, stdout, stderr) { });

    aadom.forEach(function (item, index, array) {
        var exec = require('child_process').exec;
        var cmd = 'echo ' + item + ' >> ~/recon/we-hack/' + comapny + '/raw.txt' ;
        console.log(item)
        exec(cmd, function (error, stdout, stderr) { 
        });
    })
    var exec = require('child_process').exec;
    var cmd = 'python ~/tools/we-hack/back-end/data/addon/cmd.py ' + comapny +' '+ comapny_email + '&';
    exec(cmd, function (error, stdout, stderr) {  
         console.log(error);
         console.log(stdout);
         console.log(stderr);
     });

    res.send({ title: 'ps started ' });
});

