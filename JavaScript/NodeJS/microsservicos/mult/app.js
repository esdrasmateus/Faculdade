const Koa = require('koa');
const KoaRouter = require('koa-router');

const app = new Koa();
const router = new KoaRouter();

// Routes

router.get("/mult", op1);

function op1(ctx)
{
    let hehe = ctx.search;
    let haha = hehe.indexOf("?op1=");
    let hihi = hehe.indexOf("&op2=");
    let hoho = hehe.substring(haha + 5,hihi); // 5 = número de caracteres de "?op1="
    let huhu = hehe.substring(hihi + 5,hehe.length);

    ctx.body = hoho * huhu;
}

//, ctx => (ctx.body = ctx.search));

app.use(router.routes()).use(router.allowedMethods());

app.listen(3000, () => console.log("Server started"));