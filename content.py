import fresh_tomatoes
import constructors

clube_da_luta = constructors.Movie("Clube da Luta", "2 Horas",
                                   "The two bored men form an underground club with strict rules and fight other men who are fed up with their mundane lives.",
                                   "https://ae01.alicdn.com/kf/HTB1vzb3NFXXXXbiXFXXq6xXFXXXC/Vintage-Retro-Papel-poster-anime-clube-da-Luta-Brad-Pitt-Cartaz-Cartazes-cartaz-cudi-adesivo-De.jpg",
                                   "https://www.youtube.com/watch?v=KUJOXy0e-kE")

creed2 = constructors.Movie("Creed 2", "1'9 Minutos.",
                            "In 1985, Russian boxer Ivan Drago killed former U.S. champion Apollo Creed in a tragic match that stunned the world. Against the wishes of trainer Rocky Balboa, Apollo's son Adonis Johnson accepts a challenge from Drago's son -- another dangerous fighter. Under guidance from Rocky, Adonis trains for the showdown of his life -- a date with destiny that soon becomes his obsession. Now, Johnson and Balboa must confront their shared legacy as the past comes back to haunt each man.",
                            "http://cdn.collider.com/wp-content/uploads/2018/10/creed-2-poster.jpg",
                            "https://www.youtube.com/watch?v=IS2nfJ6LVNg")

howsmovingcastle = constructors.Movie("Howls Moving Castle","1'9 Minutos",
                                      "Sophie has an uneventful life at her late father s hat shop, but all that changes when she befriends wizard Howl, who lives in a magical flying castle. However, the evil Witch of Waste takes issue with their budding relationship and casts a spell on young Sophie, which ages her prematurely. Now Howl must use all his magical talents to battle the jealous hag and return Sophie to her former youth and beauty.",
                                      "https://i.etsystatic.com/18051038/r/il/f0daa7/1628374577/il_fullxfull.1628374577_6l1q.jpg",
                                      "https://youtube.com/watch?v=iwROgK94zcM")

movies = [clube_da_luta, creed2,howsmovingcastle]
fresh_tomatoes.open_movies_page(movies)
