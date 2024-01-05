### Formatter and Sorter for Cambridge Latin story vocabulary
This program will take the word lists from a Cambridge Latin story, organize them, and quiz the user over their knowledge of the words before formatting the data into a 3-column table. <br/>

#### Program purpose:
This program was designed to help automate the formatting process of Latin vocabulary assignments, in order to facilitate easier organization and therefore learning of Latin vocabulary terms. It should be noted that using this program only eliminates the formatting part of the assignment, and that the educational value of the work is preserved when using this program. <br/>

#### Program operation:
After getting the word list from the Cambridge Latin website, the user is shown a word and asked if they either know what it means, recognize it, don't recognize it, or it isn't applicable (i.e. Latin names which cannot be translated into English). <br/>
Make sure to copy the link to the Cambridge Latin story website (example can be seen [here](https://www.dl.cambridgescp.com/sites/www.cambridgescp.com/files/legacy_root_files/singles/expall2/expnew.html?fn=ets3uk30&mn=1704383877)), before starting the program. <br/>
The program will automatically add the needed number of rows to the table, assuming that the table already has 3 columns. <br/>

#### Required Python packages:
bs4 <br/>
Selenium  <br/>
Pyperclip  <br/>
Keyboard  <br/>