# SheCoderess<V.1.0>👸💻

SheCoderess<V.1.0>, a girls only hackathon which was held on 22nd and 23rd of July 2017 at Uwa Wellassa University(UWU) of Sri Lanka. This competition is organized by the IEEE Student Branch WIE affinity group of UWU at university premises. **60 teams from 8 government and private universities** participated. Our team **UCSC Finite** won the First place. https://www.hackerearth.com/challenge/college/shecoderess-v-10-1/leaderboard/

![Team Finite](us.jpg)
<div class="image-credits"><b> IEEE Student Branch WIE Affinity Group UCSC , Dinusha Manawasinghe & Pamudi Dahanayake </b></div>


_Team members:_

  * Kalpani Bhagya Ranasinghe(myself)
  * Sandali Samarawickrama
  * Lalanga Ariyasinghe

Hope this will help you. **Pull requests are welcome.** 😇💻

__Conditions__

* Time Limit:	5.0 sec(s) for each input file.

* Memory Limit:	256 MB

* Source Limit:	1024 KB

* Marking Scheme:	Marks are awarded if any testcase passes.

* Allowed Languages:	C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Julia, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Visual Basic, Kotlin

**_01) Vowey words_**
----------------
Shanu likes to make words. She likes to find Vowely Words from Novels. If word has even number of total vowel letters (a,e,i,o,u) and vowel letter count is less than or equal square root of total character count then only it is named as Vowely Word.

First line input has T number of test queries For each T lines there is a word

For each word you need to print YES if word is Vowely and otherwise NO

SAMPLE INPUT |	SAMPLE OUTPUT 
-------------|-----------------
love	     |	Yes
wow	     |	No


Explanation
T is 2 therefore there will be 2 words wow - vowel count is odd. We print NO love - vowel count is even and 2<=2 is true (vowel letter count is less than or equal square root of total character count). We print YES

**_02) Word Count_**
---------------------

Print the number of words in a given paragraph

Assumptions

Numeric values separated by spaces are considered as words (check example)
Words do not require to have a meaning, any set of letters separated by spaces or alphanumeric characters are considered a word

SAMPLE INPUT 					   |	SAMPLE OUTPUT 
-------------------------|---------------------------------------------
8 universities... 60 teams... 180 competitors....  |	6

**_03)Fightclub mails_**
--------------------------

Sandu is the captain of Fightclub which is association of girls for women rights. She developed a system for new member registration using new programming language ballerina by WSO2. Suppose she hired you to her association as software engineer to build email validator,
Fight club email validation has these constrains

an email if valid only if, Mail domain is from this whitelist;

www.fightclub.uk

www.fightclub.com

www.fightclub.lk

www.fightclub.sa

www.fightclub.cc

www.fightclub.jp

www.fightclub.se

www.fightclub.xy

www.fightclub.gi

www.fightclub.rl

www.fightclub.ss

Username has 3 to 6 (inclusive 3,6) characters (Only lowercase English letters and numbers)

First line is number of testcases T each T line has email to validate. each line print VALID or INVALID according to above constraints

SAMPLE INPUT 			|	SAMPLE OUTPUT
------------------|-----------------
2				|	
sonia6@fightclub.com		|	VALID
am@fightclub2.lk 		|	INVALID


Explanation

sonia6@fightclub.com passed all constraints then we print VALID am@fightclub2.lk has invalid domain and not passed username constraint then we print INVALID

**_04) Word Count - same question_** 
-----------------------------------
**_05) Help the knight_**
-------------------------

(From previous DeftCoder event) Only a black knight is remaining on the chess board No other pieces... Does Knight would be able to find his shortest path to the destination ? It's on your hand... you have to find minimum number of moves he can take to reach the destination.... Please note that cordinates are from top left conor is (0,0) and bottom right conor is (7,7)...
Input Format : source cordinates. two numbers within brackets. these brackets could any type '[]', '<>'
'()' are few exmples ... or (x,y)

Output Format: Integer denoting minimum number of moves

Refer the sample input, output

SAMPLE INPUT 	|	SAMPLE OUTPUT 
--------------|---------------------
(0,0)		|	1
(2,1)		|


**_06)Binary Stream to Text_**
-------------------------------

A system is needed to be developed to read a stream of bits and converts each read 8 bits at a time into text .
The number of bit streams to read is given in the first line of the input

Constraints - The first line inputs the number of lines to be read. - Each 8 bits starting from the 1st bit in the stream represents a character. - Each of the input bit stream lines are of variable size. - If the last set of bits to be read in a line is less than 8,those bits are to be ignored.

SAMPLE INPUT 						|	SAMPLE OUTPUT 
------------------------|------------------------
2							|
011100000111100101110100011010000110111101101110	|	python
0110110001110101011000					|	lu

**_07)Missing radius_**
-----------------------

Kamalawathi is 3rd year student of CUSC University of Negombo. She is doing research to find radius of cross section of PVC pipe(Assume it is perfect cirlcle). She converts captured image to N X N square Grid. # character represents the PVC pipe portion and . character represents background. Always the center of circle falls in to middle of grid.
You are given the grid and find the integer radius of PVC pipe cross section

Input Format

First input is N Next it has the 2D grid of converted image

Note : she planned to use Euclidean distance for calculations

| SAMPLE INPUT            |     SAMPLE OUTPUT 
| ------------------------|-----------------------
| 20                      |     5
| ....................    |
| ....................    |
| ....................    |
| ....................    |
| ....................    |
| ..........#.........    |
| .......#.....#......    |
| ......#.......#.....    |
| ....................    |
| ....................    |
| .....#.........#....    |
| ....................    |
| ....................    |
| ......#.......#.....    |
| .......#.....#......    |
| ..........#.........    |
| ....................    |
| ....................    |
| ....................    |
| ....................    |
                        

**_08)Adam Numbers_**
----------------------

Find whether the given number is an Adam Number or not. Adam number is a number when reversed, the square of the number and the square of the reversed number should be numbers which are reverse of each other.

SAMPLE INPUT      |       SAMPLE OUTPUT 
------------------|-----------------------
12                |       yes

Explanation

Because given sample input is an Adam Number it prints yes. if it was otherwise answer should be no.

**_09)Soma's Cards_**
----------------------

Soma is learning Soft wear design in University of Slip. She is playing a game as per below steps.
She has N cards There is a number in both sides of a card (when they are in table only one side is visible). Each turn She can turn any cards at a time or do nothing. Once a round completes she sums all visible numbers and record it.
From those records she will find the largest number M
Finally she will decide how many cards she need to turn or not turn. She creates an array A using those turning or not turning state of cards.

Input Format

First line is N Next space seperated values of visible side of each card Final line gives space seperated values of invisible side of each card

Output Format

Display all possible turns she can do. Display the value of M and A using format as per below example
	29 ['No Turn', 'Turn', 'Turn', 'Turn']

M is 29 to get 29 she needs to do nothing for first card and turn all other cards to get other side

| SAMPLE INPUT 		|	SAMPLE OUTPUT
|-----------------------|------------------------
| 4			|	20
| 11 2 3 4		|	23
| 4 5 6 7		|	23
| 			|	26
|			|	23
|			|	26
|			|	26
|			|	29
|			|	13
|			|	16
|			|	16
|			|	19
|			|	16
|			|	19
|			|	19
|			|	22
|			|	29 ['No Turn', 'Turn', 'Turn', 'Turn']

**_10)Nadun and Fruits_**
-------------------------

Nature's candy corner is a famous fruit shop. Because of the festival season they have decided to launch a promotion. They have N fruits and let their weights be represents as w1,w2,w3,....,wN. Each fruit costs 1 unit and when a customer has a fruit with weight wX, then he can get all other fruits whose weight lies between [wX,wX+4] (both inclusive) for free.
Help Nadun who is a cunning fruit seller, trying to buy all fruits with minimum units

Input Format

The first line contains an integer i.e. number of fruits.
Next line will contain space seperated integers , representing their weights.

Constraints

1 ≤ N ≤ 10^5
0 ≤ Wi ≤ 10^4 , where i ∈ [1,N]

Output Format

Minimum units with which Nadun could buy all of fruits.

SAMPLE INPUT 		|	SAMPLE OUTPUT 
------------------------|----------------------
5			|	3
1 2 3 17 10		|

**_11)Coconut cars_**
----------------------

Amaya Constructions ltd is doing project in Badulla to help farmers by making cabel car tracks between large coconut trees.
Each coconut tree is indexed from 1 to N. Company will make M cables between different trees.

They hired you to develop mobile application which returns possibility of travelling for given start tree number and destination tree number

Input Format

First line has N and M pair
Next M lines has pairs for connectivity of trees by a cable
Next Q for number of mobile app queries
For each Q there is pair for start and end coconut tree number
Print YES if possible to travel and NO if impossible

Note : Assume when a tree between another two trees and all three trees are connected by 2 cables. Farmer can jump in to next cable car

SAMPLE INPUT 		|	SAMPLE OUTPUT 
------------------------|-----------------------
5 2			|	NO
3 4			|	YES
2 4			|
2			|
1 2			|
2 3			|

**_12)Birthday Cake Candles_**
--------------------------------

Colleen is turning n years old! Therefore, she has n candles of various heights on her cake, and candle i has height height. Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.
Given the height for each individual candle, find and print the number of candles she can successfully blow out.

Input Format

The first line contains a single integer,n , denoting the number of candles on the cake. The second line contains n space-separated integers, where each integer i describes the height of candle i.
Constraints 1 <= n <= 10^5 1 <= height <= 10^7

Output Format

Print the number of candles Colleen blows out on a new line.

SAMPLE INPUT 		|	SAMPLE OUTPUT 
------------------------|---------------------------
4			|	2
3 2 1 3			|


**_13) Substring Palindrome_**
--------------------------------

Task is to find the length of the longest Palindrome which is consists of substring of a given string. Ex :- let's say the string is "isgoodgood" the palindrome which is formed by substring could be (good)(is)(good).

SAMPLE INPUT 				|	SAMPLE OUTPUT 
----------------------------------------|--------------------------
ghiabcdefhelloadamhelloabcdefghi	|	7


**_14)Goodland Electricity_**
------------------------------

Goodland is a country with n cities, and each city Ci is sequentially numbered from 0 to n-1. These cities are connected by n-1 roads, and each road connects Ci city to its neighboring city,Ci+1 . The distance between any two cities Ci and Cj is |i-j|.
Goodland's government started a project to improve the country's infrastructure and bring electricity to its citizens. It built at most one electrical tower in every city, but they haven't turned any of them on yet. Once switched on, each tower produces enough power to provide electricity to all neighboring cities at a distance <k from the tower.
Help the goverment by finding and printing the minimum number of towers they must switch on to ensure that all Goodland's cities have electricity. If this task is not possible for the given value of k and configuration of towers, print -1.

Input Format

The first line contains two space-separated integers denoting the respective number of cities in Goodland,n , and the tower's range constant,k. The second line contains n space-separated binary integers where each integer i(0<=i<n) denotes the number of electrical towers in city Ci. Recall that the number of towers in a city will always be either 0 or 1.

Constraints

1<=k<=n<=10^5
It is guaranteed that the number of electrical towers in each city will be either 0 or 1.

Subtask

1<=k<=n<=1000 for 40% of the maximum score.

Output Format

Print a single integer denoting the minimum number of changes the government must make so that all Goodland's cities have electricity; if this is not possible for the given value of k, print -1.

SAMPLE INPUT 		|	SAMPLE OUTPUT 
------------------------|-------------------------
6 2			|	2
0 1 1 1 1 0		|
