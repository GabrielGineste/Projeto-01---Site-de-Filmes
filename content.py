import fresh_tomatoes
import constructors

#   Passando os dados que irão preencher a aplicação.
#   Filmes recebem em ordem, Title, Duration, movie_Storyline,
#                               poster_image, trailer_youtube.
clube_da_luta = constructors.Movie("Clube da Luta", "2 Horas",
                                   "Dois homens entediados, formam um clube" +
                                   " sem regras aonde lutam.",
                                   "https://ae01.alicdn.com/kf/HTB1vzb3" +
                                   "NFXXXXbiXFXXq6xXFXXXC/" +
                                   "Vintage-Retro-Papel-poster-anime-clube" +
                                   "-da-Luta-Brad-Pitt-Cartaz-Cartazes-cart" +
                                   "az-cudi-adesivo-De.jpg",
                                   "https://www.youtube.com/" +
                                   "watch?v=Fs0-4NLSO2Y")

creed2 = constructors.Movie("Creed 2",
                            "1'9 Minutos.",
                            "In 1985, Russian boxer Ivan Drago killed " +
                            "former U.S. champion Apollo Creed in a " +
                            "tragic match that stunned the world. " +
                            "Against the wishes of trainer Rocky Balboa, " +
                            "Apollo's son Adonis Johnson accepts a challenge" +
                            " from Drago's son.",
                            "http://cdn.collider.com/wp-content/uploads/" +
                            "2018/10/creed-2-poster.jpg",
                            "https://www.youtube.com/" +
                            "watch?v=IS2nfJ6LVNg")

howsmovingcastle = constructors.Movie("Howls Moving Castle",
                                      "1'9 Minutos",
                                      "Sophie has an uneventful life at " +
                                      "her late father s hat shop, but all " +
                                      "that changes when she befriends " +
                                      "wizard Howl, who lives in a magical " +
                                      "flying castle.",
                                      "https://i.etsystatic.com/18051038" +
                                      "/r/il/f0daa7/1628374577/il_full" +
                                      "xfull.1628374577_6l1q.jpg",
                                      "https://youtube.com/watch?v" +
                                      "=iwROgK94zcM")

ctrainersdragao = constructors.Movie("Como Treinar seu Dragão 3",
                                     "1'5 Horas",
                                     "Um Menino e seu Dragão amigo saem" +
                                     "em várias aventuras.",
                                     "https://www.cafecomfilme.com.br/media/" +
                                     "k2/items/cache/492cd4eee0ce1" +
                                     "274967cb54388" +
                                     "2f26a5_XL.jpg?t=1547695313",
                                     "https://www.youtube.com/watch?v=" +
                                     "P5GAg92efK0")

atomica = constructors.Movie("Atômica",
                             "1'5 Horas",
                             "Sensual and savage, Lorraine Broughton " +
                             "is the most elite spy in MI6, an" +
                             " agent who's willing to use all" +
                             " of her lethal skills to stay " +
                             "alive during an impossible mission.",
                             "https://www.metagalaxia.com." +
                             "br/wp-content/uploads/2017/" +
                             "09/atomica-poster-1.jpg",
                             "https://www.youtube.com/" +
                             "watch?v=CpF1ejZeLsE")

#   Aqui são colocados todos os objetos que estão inseridos a cima.
#   E serão executados na exibição da aplicação.
movies = [clube_da_luta, creed2, howsmovingcastle,
          ctrainersdragao, atomica]
#   Função que executa a criação do arquivo HTML.
fresh_tomatoes.open_movies_page(movies)
