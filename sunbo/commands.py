import click
import  time
from sunbo import app,db
from sunbo.models import User,Ariticles
# 自定义initdb
@app.cli.command()
@click.option('--drop',is_flag=True,help='删除之后再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库')

# 自定义命令forge，把数据写入数据库
@app.cli.command()
def forge():
    db.create_all()
    author = "SunBo"
    ariticles = [
        {'title': '战疫小赋', 'content': '鼠年春节将至，突遭新冠疫情。明日山花烂漫，你我笑谈人生。'},
        {'title': '向热爱致敬！', 'content': '在NBA效力了22年、已经43岁的卡特在场上依然会为了一次球权飞身救球，全力以赴就是自己对初心最好的交代！'},
        {'title': '学习强国', 'content': '习近平总书记关切事｜确保不误农时，保障夏粮丰收——各地抓好春耕生产在行动'},
        {'title': '你认为这个判罚是否合理？', 'content': '#孙杨遭禁赛8年# 你认为这个判罚是否合理？ R新浪体育的微博投票 ????'},
        {'title': '疫情期间，你的工资有变化吗？',
         'content': '疫情突如其来，许多企业的生产经营，遇到了程度不同的困难。近期，财政部出台调整部分企业所得税、免征部分行业增值税等政策减轻企业负担，央行也通过专项贷款等措施推动企业复工复产'},
        {'title': '【塞斯-库里37+2+2实录】',
         'content': '今日独行侠客场落败，独行侠球员塞斯-库里表现出色，首发出战36分钟，15投13中，其中三分球9投8中，得到37分2篮板2助攻，其中37分是小库里生涯得分新高，8记三分也创造了单场命中三分纪录！姓库里的都很准！'},
        {'title': '乔治单臂暴扣', 'content': '伦纳德长臂一伸成功抢断快船发动反击，保罗-乔治接球冲筐单臂暴扣'},
        {'title': '罗斯31分集锦',
         'content': '今夜玫瑰绽放[鲜花]活塞客场挑战太阳，德里克-罗斯在30分钟的出场时间里，24投15中砍下31分4助攻3篮板2抢断1盖帽的全面数据。末节太阳疯狂追分，是罗斯连得4分帮助活塞捍卫胜果，射落太阳，终结7连败。来回顾罗斯今日超强表现！'},
        {'title': '音乐知识', 'content': '扎西尼玛现场深情演唱一首《向往神鹰》，特有的豪迈之情，太赞了'},
        {'title': '范巴斯滕', 'content': '范巴斯滕：说C罗比梅西强 要么不懂球要么在撒谎'}
    ]
    user = User(author=author)
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    db.session.add(user)
    for m in ariticles:
        ariticles = Ariticles(title=m['title'],content=m['content'],pubdate=localtime)
        db.session.add(ariticles)
    db.session.commit()
    click.echo('数据导入完成')

# 生成admin账号的函数
@app.cli.command()
@click.option('--username',prompt=True,help="用来登录的用户名")
@click.option('--password',prompt=True,hide_input=True,confirmation_prompt=True,help="用来登录的密码")
def admin(username,password):
    db.create_all()
    user = User.query.first()
    if user is not None:
        click.echo('更新用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建用户')
        user = User(userauthor=username,author="雷洛")
        user.set_password(password)
        db.session.add(user)
    
    db.session.commit()
    click.echo('创建管理员账号完成')