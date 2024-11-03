var express = require('express');
var fs = require('fs');
var app = express();


app.set('view engine', 'ejs');



// index page
app.get('/', function(req, res) {
  res.render('pages/index');
});

// challenge endpoint
app.get('/ctf', function(req, res) {
    if (!req.query.lang) {
        res.status(400).send();
        return;
    }
    const filename = 'views/paragraphs/' + req.query.lang;
    res.setHeader("Content-Type","text/html; charset=utf-8");

    fs.readFile(filename, (err, data) => {
        if (err) {
        res.status(500).send("<p>Sorry this lang does not exist !</p>");
        }    
        res.status(200).send(data);
    });
});

app.listen(5001);
console.log('Server is listening on port 5001');