# ######################
#       Readme         #
# Submission for Uber  #
# By - Pratyush Swamy  #
# ######################

I prefer to work on the back-end and therefore I implemented the command line version of the Email Service.
I've worked on back-end technologies for over 5 yrs but have no professional experience. Back End is where data is
handled and manipulated. Behind the scenes.

###########################################################################
Details of the Challenge - Email Service.
###########################################################################
1. I've used Python 3.3.2. Lower versions might not be able to run the program properly.
2. Used Mailgun and Mandrill for email services. Username/Password are in the program for convenience.
3. The implementation warrants use of second service (here it will be Mailgun), if Mandrill fails because of any reason.
4. The program can send emails to multiple users at the same time.
5. I've used smtp libraries available in Python. No APIs of Mailgun or Mandrill were used.

Test -
    6. To test this, please make any changes to the 'pass_mandrill'. The program will mention Mandrill has failed
    and then call Mailgun.

P.S - Altering 'user_mandrill' alone will not fail the service. This is a bug in their service. Even the wrong username
with a "correct" password sends the emails. Also, while sending emails to multiple people, Mandrill shows the emails of
all the users in CC by default. This is not the case with Mailgun.