const Koa = require("koa");
const json = require("koa-json");
const KoaRouter = require("koa-router");
const path = require("path");
const render = require("koa-ejs");

const app = new Koa();
const router = new KoaRouter();

// Replace with db

const things = ["My Family", "Programming", "Music"];

// Json prettier Middleware

app.use(json());

// Simple Middleware Example
//app.use(async ctx => ctx.body = { msg: "JSON TEST"});

render(app,{
    root: path.join(__dirname, "views"),
    layout: "layout",
    viewExt: "html",
    cache: false,
    debug: false
});

// Routes

router.get("/", index);
router.get("/add", showAdd);

// List of things

async function index(ctx){
    await ctx.render("index", {
        title: "Things I Love: ",
        things: things
    });
}

// Show Add Page

async function showAdd(ctx){
    await ctx.render("add");
}

router.get("/test", ctx => (ctx.body = "Hello Test"));

// Router Middleware

app.use(router.routes()).use(router.allowedMethods());

app.listen(3000, () => console.log("Server started"));