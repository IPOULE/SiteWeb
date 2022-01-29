from website import create_app, db
from website.models import Livre

if __name__ == '__main__':
    flask_app = create_app()
    with flask_app.app_context():
        db.create_all()
        l1 = Livre('Machine Learning', '20/12/2020', '20', 'https://mrmint.fr/wp-content/uploads/2017/03/Data-science-octo-300x300.jpg')
        l2 = Livre('Les bases de données NoSQL','10/11/2019','22','https://servimg.eyrolles.com/static/media/1559/9782212141559_internet_h1400.jpg')
        l3 = Livre('Data Science avec Python','16/11/2021','26','https://images.epagine.fr/461/9782412053461_1_75.jpg')
        l4 = Livre('Hadoop par la pratique','30/12/2018','16','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHHCg5Pis6m8o1m2Vu63OojYoD9radq9z2ZA&usqp=CAU')
        l5 = Livre('Machine Learning','20/12/2020','29','https://mrmint.fr/wp-content/uploads/2017/03/Data-science-octo-300x300.jpg')
        l6 = Livre('Apache Sparkig','20/09/2020','30','https://www.prologue.ca/DATA/LIVRE/grande/9782409033780.jpg')
        l7 = Livre('Analyse prédictive','23/04/2020','27','https://images.lavoisier.net/couvertures/1317672459.jpg')
        l8 = Livre('Python  avec Numpy, Pandas, Matplotlib et Seaborn','20/12/2020','20$','https://mrmint.fr/wp-content/uploads/2017/03/Data-science-octo-300x300.jpg')
        l9 = Livre('Data Engineering and application','06/12/2019','35','https://images.lavoisier.net/couvertures/1317596933.jpg')
        l10 = Livre('Data Science strategy','01/08/2021','34','https://images.lavoisier.net/couvertures/1317185952.jpg')
        l11 = Livre('Learning','1/12/2021','40','https://images-na.ssl-images-amazon.com/images/I/419L2K0TYIL._SX350_BO1,204,203,200_.jpg')
        db.session.add_all([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11])
        db.session.commit()
