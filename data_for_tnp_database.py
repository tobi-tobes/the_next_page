#!/usr/bin/python3
""" Dump for The Next Page """
from models import *

# creation of Books
the_hunger_games = book.Book(title='The Hunger Games',
                  author='Suzanne Collins',
                  pub_date='2008-09-14',
                  age_category='Young Adult',
                  page_length=374,
                  fiction=True,
                  description="In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV.\nSixteen-year-old Katniss Everdeen, who lives alone with her mother and younger sister, regards it as a death sentence when she steps forward to take her sister's place in the Games. But Katniss has been close to dead before - and survival, for her, is second nature. Without really meaning to, she becomes a contender. But if she is to win, she will have to start making choices that weight survival against humanity and life against love.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1586722975i/2767052.jpg')
the_hunger_games.save()

the_kite_runner = book.Book(title='The Kite Runner',
                  author='Khaled Hosseini',
                  pub_date='2003-05-29',
                  age_category='Adult',
                  page_length=371,
                  fiction=True,
                  description="1970s Afghanistan: Twelve-year-old Amir is desperate to win the local kite-fighting tournament and his loyal friend Hassan promises to help him. But neither of the boys can foresee what would happen to Hassan that afternoon, an event that is to shatter their lives. After the Russians invade and the family is forced to flee to America, Amir realises that one day he must return to an Afghanistan under Taliban rule to find the one thing that his new world cannot grant him: redemption.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1579036753i/77203.jpg')
the_kite_runner.save()

the_book_thief = book.Book(title='The Book Thief',
                  author='Markus Zusak',
                  pub_date='2005-03-01',
                  age_category='Young Adult',
                  page_length=552,
                  fiction=True,
                  description="It is 1939. Nazi Germany. The country is holding its breath. Death has never been busier, and will be busier still.\nBy her brother's graveside, Liesel's life is changed when she picks up a single object, partially hidden in the snow. It is The Gravedigger's Handbook, left behind there by accident, and it is her first act of book thievery. So begins a love affair with books and words, as Liesel, with the help of her accordian-playing foster father, learns to read. Soon she is stealing books from Nazi book-burnings, the mayor's wife's library, wherever there are books to be found.\nBut these are dangerous times. When Liesel's foster family hides a Jew in their basement, Liesel's world is both opened up, and closed down.\nIn superbly crafted writing that burns with intensity, award-winning author Markus Zusak has given us one of the most enduring stories of our time.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1522157426i/19063.jpg')
the_book_thief.save()

harry_potter_seven = book.Book(title='Harry Potter and the Deathly Hallows',
                  author='J.K. Rowling',
                  pub_date='2007-07-21',
                  age_category='Young Adult',
                  page_length=759,
                  fiction=True,
                  description="Harry has been burdened with a dark, dangerous and seemingly impossible task: that of locating and destroying Voldemort's remaining Horcruxes. Never has Harry felt so alone, or faced a future so full of shadows. But Harry must somehow find within himself the strength to complete the task he has been given. He must leave the warmth, safety and companionship of The Burrow and follow without fear or hesitation the inexorable path laid out for him...\nIn this final, seventh installment of the Harry Potter series, J.K. Rowling unveils in spectacular fashion the answers to the many questions that have been so eagerly awaited.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1663805647i/136251.jpg')
harry_potter_seven.save()

the_help = book.Book(title='The Help',
                  author='Kathryn Stockett',
                  pub_date='2009-02-10',
                  age_category='Adult',
                  page_length=464,
                  fiction=True,
                  description="Three ordinary women are about to take one extraordinary step...\nSeemingly as different from one another as can be, these women will nonetheless come together for a clandestine project that will put them all at risk. And why? Because they are suffocating within the lines that define their town and their times. And sometimes lines are made to be crossed.\nIn pitch-perfect voices, Kathryn Stockett creates three extraordinary women whose determination to start a movement of their own forever changes a town, and the way women, mothers, daughters, caregivers, friends, view one another. A deeply moving novel filled with poignancy, humor, and hope, The Help is a timeless and universal story about the lines we abide by, and the ones we don't.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1622355533i/4667024.jpg')
the_help.save()

life_of_pi = book.Book(title='Life of Pi',
                  author='Yann Martel',
                  pub_date='2001-09-11',
                  age_category='Adult',
                  page_length=460,
                  fiction=True,
                  description="Life of Pi is a fantasy adventure novel by Yann Martel published in 2001. The protagonist, Piscine Molitor 'Pi' Patel, a Tamil boy from Pondicherry, explores issues of spirituality and practicality from an early age. He survives 227 days after a shipwreck while stranded on a boat in the Pacific Ocean with a Bengal tiger named Richard Parker.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1631251689i/4214.jpg')
life_of_pi.save()

girl_with_dragon_tattoo = book.Book(title='The Girl with the Dragon Tattoo',
                  author='Stieg Larsson',
                  pub_date='2005-08-01',
                  age_category='Adult',
                  page_length=480,
                  fiction=True,
                  description="Harriet Vanger, a scion of one of Sweden's wealthiest families disappeared over forty years ago. All these years later, her aged uncle continues to seek the truth. He hires Mikael Blomkvist, a crusading journalist recently trapped by a libel conviction, to investigate. He is aided by the pierced and tattooed punk prodigy Lisbeth Salander. Together they tap into a vein of unfathomable iniquity and astonishing corruption.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1684638853i/2429135.jpg')
girl_with_dragon_tattoo.save()

beach_read = book.Book(title='Beach Read',
                  author='Emily Henry',
                  pub_date='2020-05-19',
                  age_category='Adult',
                  page_length=400,
                  fiction=True,
                  description="Augustus Everett is an acclaimed author of literary fiction. January Andrews writes bestselling romance. When she pens a happily ever after, he kills off his entire cast.\nThey're polar opposites.\nIn fact, the only thing they have in common is that for the next three months, they're living in neighboring beach houses, broke, and bogged down with writer's block.\nUntil, one hazy evening, one thing leads to another and they strike a deal designed to force them out of their creative ruts: Augustus will spend the summer writing something happy, and January will pen the next Great American Novel. She'll take him on field trips worthy of any rom-com montage, and he'll take her to interview surviving members of a backwoods death cult (obviously). Everyone will finish a book and no-one will fall in love. Really.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1589881197i/52867387.jpg')
beach_read.save()

charlotte = book.Book(title="Charlotte's Web",
                  author='E.B. White',
                  pub_date='1952-10-15',
                  age_category='Children',
                  page_length=184,
                  fiction=True,
                  description="Some Pig. Humble. Radiant. These are the words in Charlotte's Web, high up in Zuckerman's barn. Charlotte's spiderweb tells of her feelings for a little pig named Wilbur, who simply wants a friend. They also express the love of a girl named Fern, who saved Wilbur's life when he was born the runt of his litter.\nE. B. White's Newbery Honor Book is a tender novel of friendship, love, life, and death that will continue to be enjoyed by generations to come. This edition contains newly color illustrations by Garth Williams, the acclaimed illustrator of E. B. White's Stuart Little and Laura Ingalls Wilder's Little House series, among many other books.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1628267712i/24178.jpg')
charlotte.save()

hungry_caterpillar = book.Book(title="The Very Hungry Caterpillar",
                  author='Eric Carle',
                  pub_date='1969-06-03',
                  age_category='Children',
                  page_length=26,
                  fiction=True,
                  description="One sunny Sunday, the caterpillar was hatched out of a tiny egg. He was very hungry. On Monday, he ate through one apple; on Tuesday, he ate through three plums--and still he was hungry. When full at last, he made a cocoon around himself and went to sleep, to wake up a few weeks later wonderfully transformed into a butterfly!\nThe brilliantly innovative Eric Carle has dramatized the story of one of Nature's commonest yet loveliest marvels, the metamorphosis of the butterfly. This audiobook will delight as well as instruct the very youngest listener.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1603739265i/4948.jpg')
hungry_caterpillar.save()

short_history = book.Book(title="A Short History of Nearly Everything",
                  author='Bill Bryson',
                  pub_date='2003-01-01',
                  age_category='Adult',
                  page_length=544,
                  fiction=False,
                  description="Bill Bryson describes himself as a reluctant traveller, but even when he stays safely at home he can't contain his curiosity about the world around him. \"A Short History of Nearly Everything\" is his quest to understand everything that has happened from the Big Bang to the rise of civilisation - how we got from there, being nothing at all, to here, being us. The ultimate eye-opening journey through time and space, revealing the world in a way most of us have never seen it before.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1433086293i/21.jpg')
short_history.save()

outliers = book.Book(title="Outliers: The Story of Success",
                  author='Malcolm Gladwell',
                  pub_date='2008-11-18',
                  age_category='Adult',
                  page_length=309,
                  fiction=False,
                  description="In this stunning book, Malcolm Gladwell takes us on an intellectual journey through the world of \"outliers\" - the best and the brightest, the most famous and the most successful. He asks the question: what makes high-achievers different?\nHis answer is that we pay too much attention to what successful people are like, and too little attention to where they are from: that is, their culture, their family, their generation, and the idiosyncratic experiences of their upbringing. Along the way he explains the secrets of software billionaires, what it takes to be a great soccer player, why Asians are good at math, and what made the Beatles the greatest rock band.\nBrilliant and entertaining, Outliers is a landmark work that will simultaneously delight and illuminate.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1344266315i/3228917.jpg')
outliers.save()

meaning = book.Book(title="Man's Search for Meaning",
                  author='Viktor E. Frankl',
                  pub_date='1959-01-01',
                  age_category='Adult',
                  page_length=165,
                  fiction=False,
                  description="Psychiatrist Viktor Frankl's memoir has riveted generations of readers with its descriptions of life in Nazi death camps and its lessons for spiritual survival. Based on his own experience and the stories of his patients, Frankl argues that we cannot avoid suffering but we can choose how to cope with it, find meaning in it, and move forward with renewed purpose. At the heart of his theory, known as logotherapy, is a conviction that the primary human drive is not pleasure but the pursuit of what we find meaningful. Man's Search for Meaning has become one of the most influential books in America; it continues to inspire us all to find significance in the very act of living.",
                  cover_image='https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1535419394i/4069.jpg')
meaning.save()

# creation of Genres
dystopia = genre.Genre(name="Dystopia", parent_genre="Fiction")
dystopia.save()

science_fiction = genre.Genre(name="Science Fiction", parent_genre="Fiction")
science_fiction.save()

fantasy = genre.Genre(name="Fantasy", parent_genre="Fiction")
fantasy.save()

romance = genre.Genre(name="Romance", parent_genre="Fiction")
romance.save()

adventure = genre.Genre(name="Adventure", parent_genre="Fiction")
adventure.save()

historical = genre.Genre(name="Historical Fiction", parent_genre="Fiction")
historical.save()

drama = genre.Genre(name="Drama", parent_genre="Fiction")
drama.save()

war = genre.Genre(name="War", parent_genre="Fiction")
war.save()

contemporary = genre.Genre(name="Contemporary", parent_genre="Fiction")
contemporary.save()

chick_lit = genre.Genre(name="Chick Lit", parent_genre="Fiction")
chick_lit.save()

magical_realism = genre.Genre(name="Magical Realism", parent_genre="Fiction")
magical_realism.save()

classics = genre.Genre(name="Classics", parent_genre="Fiction")
classics.save()

mystery = genre.Genre(name="Mystery", parent_genre="Fiction")
mystery.save()

thriller = genre.Genre(name="Thriller", parent_genre="Fiction")
thriller.save()

suspense = genre.Genre(name="Suspense", parent_genre="Fiction")
suspense.save()

crime = genre.Genre(name="Crime", parent_genre="Fiction")
crime.save()

picture = genre.Genre(name="Picture Books", parent_genre="Fiction")
picture.save()

physics = genre.Genre(name="Physics", parent_genre="Non-Fiction")
physics.save()

history = genre.Genre(name="History", parent_genre="Non-Fiction")
history.save()

humor = genre.Genre(name="Humor", parent_genre="Non-Fiction")
humor.save()

science = genre.Genre(name="Science", parent_genre="Non-Fiction")
science.save()

philosophy = genre.Genre(name="Philosophy", parent_genre="Non-Fiction")
philosophy.save()

psychology = genre.Genre(name="Psychology", parent_genre="Non-Fiction")
psychology.save()

sociology = genre.Genre(name="Sociology", parent_genre="Non-Fiction")
sociology.save()

self_help = genre.Genre(name="Self Help", parent_genre="Non-Fiction")
self_help.save()

personal_dev = genre.Genre(name="Personal Development", parent_genre="Non-Fiction")
personal_dev.save()

memoir = genre.Genre(name="Memoir", parent_genre="Non-Fiction")
memoir.save()

spirituality = genre.Genre(name="Spirituality", parent_genre="Non-Fiction")
spirituality.save()

biography = genre.Genre(name="Biography", parent_genre="Non-Fiction")
biography.save()

# link books with genres
the_hunger_games.genres.append(dystopia)
the_hunger_games.genres.append(science_fiction)
the_hunger_games.genres.append(fantasy)
the_hunger_games.genres.append(romance)
the_hunger_games.genres.append(adventure)

the_kite_runner.genres.append(drama)
the_kite_runner.genres.append(contemporary)
the_kite_runner.genres.append(historical)

the_book_thief.genres.append(historical)
the_book_thief.genres.append(war)

harry_potter_seven.genres.append(fantasy)
harry_potter_seven.genres.append(adventure)

the_help.genres.append(historical)
the_help.genres.append(chick_lit)
the_help.genres.append(contemporary)

life_of_pi.genres.append(fantasy)
life_of_pi.genres.append(adventure)
life_of_pi.genres.append(contemporary)
life_of_pi.genres.append(magical_realism)

girl_with_dragon_tattoo.genres.append(contemporary)
girl_with_dragon_tattoo.genres.append(mystery)
girl_with_dragon_tattoo.genres.append(thriller)
girl_with_dragon_tattoo.genres.append(crime)
girl_with_dragon_tattoo.genres.append(suspense)

beach_read.genres.append(chick_lit)
beach_read.genres.append(contemporary)
beach_read.genres.append(romance)

charlotte.genres.append(fantasy)
charlotte.genres.append(classics)

hungry_caterpillar.genres.append(classics)
hungry_caterpillar.genres.append(picture)

short_history.genres.append(science)
short_history.genres.append(history)
short_history.genres.append(physics)
short_history.genres.append(humor)
short_history.genres.append(philosophy)

outliers.genres.append(psychology)
outliers.genres.append(self_help)
outliers.genres.append(personal_dev)
outliers.genres.append(sociology)

meaning.genres.append(history)
meaning.genres.append(self_help)
meaning.genres.append(personal_dev)
meaning.genres.append(biography)
meaning.genres.append(memoir)
meaning.genres.append(philosophy)
