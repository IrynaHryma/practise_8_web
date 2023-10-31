from models import Quote,TextPost, Author



if __name__=="__main__":
    albert= Author(fullname='Albert Einstein', born_date='March 14, 1879', born_location='in Ulm, Germany').save()
    
    
    post1 = TextPost(quote="“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”", author=albert)
    post1.tags = ["change","deep-thoughts","thinking","world"]
    post1.save()

    post2 = TextPost(quote="“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”", author=albert)
    post2.tags = ["inspirational","life","live","miracle","miracles" ]
    post2.save()

    post3  = TextPost(quote="“Try not to become a man of success. Rather become a man of value.”", author=albert)
    post3.tags = [ "adulthood","success","value"]
    post3.save()
    
    
    
    steve = Author(fullname='Steve Martin', born_date='August 14, 1945', born_location='in Waco, Texas, The United States').save()

    post4 = TextPost(quote="“A day without sunshine is like, you know, night.”", author=steve)
    post4.tags = [ "humor","obvious","simile"]
    post4.save()