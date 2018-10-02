#Worksheet 1 - welcome to R

Welcome to the second part of the Bioinformatics class! 

As you know, the first part of the class focused on Perl, the command line and emacs. This second part of the class will focus on R. It is taught by me, Daniel Fulop. We'll do R for 5 weeks and after that, you have another 3.5 weeks to work on your projects. 

In this class, you will be mostly working by yourself or with a partner. You get worksheets and work at your own pace. Worksheets are due 1 week after they're assigned in class. If you turn them in late, you will be deducted 10% for each day late. I am working on a means of digital submission of worksheets ~~probably through iLearn~~ through GitHub.

**Task 1** - Be a class ambassador and visit my office hours. 

**Goal:** Each day of the course (except day 1), I would like to know how you are doing. I also would like to get to know everyone. Each of you should therefore sign up to come to my office hours once during the coming 5 weeks. My office hours are Tuesday and Thursday 1:30-2:30. Use this sign up spreadsheet: https://goo.gl/4rw9i6


When you come to my office hours (probably with a colleague), be prepared to tell me at least one thing you found interesting in the last class and one thing you found confusing, hard or boring. Office hours will be held in this computer lab.

**Did you sign up for an office hour meeting?**

**Yes** / No


Name: Ryan Kyger


Date: 10/25

***  
#Worksheet 2 - R inspiration

R is a software environment and programming language for statistics that is used by many people, among them many biologists. The goal of this worksheet is for you to find inspiration to learn R by reading about how other people use R and how these people got started with R. 

####Task 1 - read four stories from https://whyiuser.wordpress.com/
Go to the website, pick a story that looks like it could be interesting and answer the following questions. Repeat four times.

**Story #1:**

1. What is the R user's name? Robert M Flight 

2. What topic do they work on? 

	Bioinformatics of multi-omics (transcriptomics, genomics, metabolomics)

3. Which answer did you find most surprising / what did you learn from reading their story?

	I learned that R can be used to quickly visualize data. 

**Story #2:**

1. What is the R user's name? Stephen Piccolo

2. What topic do they work on? Cancer Genomics

3. Which answer did you find most surprising / what did you learn from reading their story?  

	I learned that R syntax and behavior can be inconsistent across different packages.
	


**Story #3:**

1. What is the R user's name? Ed Connor

2. What topic do they work on? Ecology and Evolutionary Biology

	I learned that R can be used for non-linear modeling. 

3. Which answer did you find most surprising / what did you learn from reading their story?  

	I learned that ggplot is supposedly something very useful in R. 


**Story #4:**

1. What is the R user's name? Paola Cognigni

2. What topic do they work on? 
	Drosophila neuroscience

3. Which answer did you find most surprising / what did you learn from reading their story?  
	I learned that ggplot is supposedly something very useful in R. 



####Task 2 - summarize

After reading several stories about people who use R, is there anything problem that you think R can help you to solve? Is there anything particular that caught your interest?

Its sounds like R is a better tool than Excel for making data plots; I am excited about this as this will be useful for my research. I also heard that R can be used for machine learning and non-linear modeling, these are things that I might work with someday. 


Is there anything that didn't make sense to you or was unexpected? 

I learned that R has more capabilities than I previously thought and I would like to learn more about this “ggplot”. 


####Task 3 - share with your neighbor
Compare notes with at least one neighbor. Why did you neighbor choose the stories he or she read? Did you pick up something different? Did the stories change your ideas about R?

They read some of the same stories. The stories made me realized that R has more capabilities than I previously thought. 

**Finished!** 

Name: 

Date:  

***

#Worksheet 3 - Do chapter 1 of online R tutorial https://www.codeschool.com/courses/try-r

You need to create a login for Codeschool, then you get started with the R class.  
For this worksheet, you'll do chapter 1. 

1. Do you see any differences with Perl? Write down at least 3 differences

	Yes, printing does not require a print command, functions use parentheses (i.e. sum()), and running a code in file requires the source() command.


2. How would you ask R to multiply 7 and 8? Or to divide 7 by 8? 

	7*8 ; 7/8


3. Which of the following expressions would return a logical (or boolean) value? 

* A. `3 < 4` yes, TRUE
* B. `3 == 4` yes, FALSE
* C. `x <- 4` nope
* D. `4 -> x` nope

4. Can you assign a logical value to a variable called "y"? How would you assign FALSE to a variable called "y"? 

	Yes, you can assign a logical value to a variable called “y”; y = FALSE

5. Name three functions you learned in the tutorial. What do they do? 

	sum(), sums a list of numbers together
	
	rep(), repeated printing of a string
	
	sqrt(), find the square root of a value

6. What is the function you use to list all the files in your current directory?

	list.files() 


7. What is the function you use to run all the code in a file called "file.R"? 

	source(“file.R”)

8. Do you have any questions about the tutorial? 

	Nope, but I like how R is similar to python.


**Finished!**

Name: 


Date:  

***

#Worksheet 4 - Do chapter 2 of online R tutorial http://tryr.codeschool.com/

Login to Codeschool and do chapter 2.

1. Define the following data structures? What do you find written in them?

	Boolean: data type with two possible values; TRUE or FALSE

	Numeric: data type with numerical values; 1 2 3 4

	String: data type with characters; “a” “1”, “%”

2. What happens if you try to combine in a vector a Boolean, a numeric and a string? 

	All the values get converted to characters, so that the vector can hold them all.

3. What would be the result of this piece of code: `seq(1, 2, 0.1)`Type it in to RStudio!

	1.0 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.0 

4. A vector can have names. How do you call an element of a vector by its name

	First you assign names to a vector's elements by creating a second vector filled with the names you want using the names() function and then you can call a vector element by putting the name in brackets (i.e. vector[“name”]).

5. Suppose you'd run this code to make a vector:  
`sentence <- c("I", "am", "not", "learning", "R", "!", "!")` and then you'd run this code: `sentence[c(1,2,4,5)]`  
What would be the output?  
Does R start counting at 0 or at 1?  
Is this different from Perl? 

	“I” “am” “learning” “R”. Yes, R starts counting at 1, Perl starts counting at 0.

6. In chapter 2 of the online R tutorial on Codeschool, you'll learn how to make two kinds of plots. What are they? What functions do you use to make them? In each case, what goes on the x-axis and what on the y-axis? 

	Barplots and Scatter plots; barplot() and plot()

	barplot(stuff that goes on the x-axis)

	plot(stuff that goes on the x-axis, stuff that goes on the y-axis)


**Finished!** 

Name: 

Date:
