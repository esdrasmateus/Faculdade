const express = require('express');
const app = express();
const morgan = require('morgan');
const mongoose = require('mongoose');
const config = require('config');

const userRouter = require("./Routes/user");
const dbConfig = config.get("esdras.dbConfig.dbName");

mongoose.connect(dbConfig, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(()=>{
    console.log("Database Connected");
}).catch(err => {
    console.log("Database not connected " + err.message);
});

app.use(morgan("dev"));

app.use(express.json());

app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-headers",
    "Origin, X-Requested-With, Content-Type, Accept, Authorization");

    if (req.method === "OPTIONS") {
        res.header("Access-Control-Methods", "PUT, POST, PATCH, DELETE, GET");
        return res.status(200).json({

        })
    }
    next();
})

app.use("/user", userRouter);

app.use((req, res, next) => {
    const error = new Error("Not Found");
    next(error);
});

app.use((error, req, res, next) => {
    res.status(error.status || 500);
    res.json({ 
        error:{
            message:error.message
        }
    })
})

module.exports = app;