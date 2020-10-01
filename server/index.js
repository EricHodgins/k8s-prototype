const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
app.use(cors());
app.use(bodyParser.json());

const DB = 'mongodb://mongo-cluster-ip-service:27017/test';
mongoose.connect(DB, {
    useNewUrlParser: true,
    useCreateIndex: true,
    useFindAndModify: true
}).then(() => {
    console.log('Connected to MongoDB from server...');
});

// Routes
app.get('/', (req, res) => {
    res.send('Making progress. This will be legendary.');
});

app.listen(3000, (err) => {
    console.log('Listening on port 3000..');
})