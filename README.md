# Convert images to ASCII art with Python

## About ASCII-ART
ASCII-ART is a python script that converts images to ASCII art.

For example, when the following image of a dinosaur - 
![dinosaur](samples/images/dino.png)

will be converted to an image such as (width of image can be adjusted)-

```text
                                                           ,::.                                     
                                                       .@@&*++:@@:                                  
                                                     ,@&,,,,,,,,,*@                                 
                                                    #8,,,,,,,,,,,,,@,                               
                                                   #:,,,,,,,,,,,,,,,@.                              
                                                  #*,,,,,,,,,,,,,,,,,@                              
                                                 oo+,,,,,,,,,,,,,,,,,,#                             
                                                .@+,,,,,,,,,,,,,,,,,,,@+                            
                                                @++,,,,,,+++:o::*,,,,,,@                            
                                               +&++,,,,,++:o8@@@@&+,,,,8.                           
                                               @*++,,,+++:o@@+   +@+,,,+8 +o&888&:+.                
                                              .8*+++++++*o@@       @+,,,@8:++,,,++:&@@#*            
                                              8**+++++++o&@     .,  *,,+@,,,,,,,,,,,,,+8@#.         
                                             *#**++++++*o@&     ,::,8+++8,,,,,,,,,,,,,,,,,##        
                                            .@***++++++oo@      ::::.+++*,,,+,,,,,,,,,,,,,,+@       
                                            @****++++++o8@      ::::::+++,++++,+,,,,,,,,,,,,+@      
                                           8:***+++++++o@&     :&&o:::+++++++++++,,,,,,,,,,,,8,     
                                           @****+++++++o@:   *:&&&&::*++++++++++++++,,,,,,,,:,#     
                                          @****++++++++o@*   ::&&&&::*+++++++++++++++++,,,,&@:@     
                                          @****++++++++o#o   :::&&o::*+++++++++++++++++++++#@o8     
                                         +:****++++++++oo@   ::::::::*+++++++++++++++++++++&@oo.    
                                         @::**+++++++++:o@   .::::::,+++++++++++++++++++++++@oo.    
                                         @::::+++++++++*o#+   +::.  ,+++++++++++++++++++++++**&.    
                                         #::::**++++++++oo@    .*   ++++++++++++++++++++++++++8     
                                         8:::******++++++oo@       :++++++++++++++++++++++++++@     
                                         &::::*******+*++*oo#.   .o+++++++++++++++++++++++++++@     
                                         8::::**********+*+oooooo*++++++++++++++++++++++++++++&     
                                         8::::**************+***+++++++++++++++++++++++++++++&.     
                                         @:::::+,,,,,,,,,+****++***++++++++++++++++++++++++++@      
                                        ,#:::8+,........,,.*&::::::****++++++++++++++++++++++8      
                                        @,::o+,............,,*@:::::::****++++++++++++++++++#.      
                                        @+*@++,...,..........,,##:::::::**:***++++++++++++++#       
                                       ::+o++++,,,,,,,,,..,,....,@@@@@@#&@@******++++++++++@        
                                       @,+@++++,,,,,,,,,,,,,,,,,.,&@#: .#. @@#:*:::**+++**&:        
                                       @++@+++++,,,,,,,,,,,,,,,,,,,,.&@@8+.@# *@8,8:*****&8         
                                       @++8++++++,,,,,,,,,,,,,,,,,,,,,,,.*#@@88&. @&@@@@@+          
                                      .#++*:++++++,,,,,,,,,,,,,,,,,,,,,,,,,,,,*&@@@@@@@@@           
                                      +o+++@++++++++,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..,,8           
                                      o*+++&*+++++++++,,,,,,++++,,,,,,,,,,,,,,,,,,,,,,,+@           
                                      &+++++@++++++++++++++++++++++,,,,,,,,,,,,,,,,,,++*&           
                                      8++++++@:+++++++++++++++++++++++++++++,,,,,,++++*@            
                                      #+++++++&@+++++++++++++++++++++++++++++++++++++@&             
                                      8++++++++*#@o++++++++++++++++*o&&&8888#@@@@@@@:               
                                      &+++&+++++**:#@@@o:**:o@@@8o+....                             
                                      o*+@+,,,++*o*,,,,,*::@.                                       
                                      o*&+,,,,,+*:&+,,,,,,,:8                                       
                                      :*@,,,,,,+*:@*,,,,,,,,@.                                      
                                      :88,,,,,+**:&o,,,,,,,,,@                                      
                                      o@+,,,,++*::&8+,,,,,,,,:#                                     
                                      8@+,,,++**::@:+,,,,,,,,,@,                                    
     8,                               @@+++++**:::@+++,,,,,,,,,@                                    
    @+#8                              @*+++++**::@o++++,,,,,,,,:8                                   
   *&,+&@                            +@+++++**::@8+++++,,,,,,,,,@                                   
   @.,++*@.                         .@o+++*:**:@#+++++++,,,,,,,,,#                                  
   @..++++@,                        @@+++++*@::@++++++++,,,,,,..,@                                  
   @...++++@@                      #:@+++++*:@@:+++++++++,,,,,..,+&                                 
   #+,,++++++@#                  .@*:@+,++++*#@++++++++++,,,,....,@                                 
   ::,,,+++++++@@*             o@#8++@,,,++++:@:+++++++++,,,,....,#.                                
   .@+,,++++++++,o@@@@#88##@@@#+++++*:@,,++++*o@**++++++++,,......,8 .                              
    @+,,,++++++++++++++++++++++++**:++@+,++++*:#@@@@&+++++,.......,@#8@@                            
    .#+,,,+++++++++++++++++++++++:++++*@+,+++**::::#,@@+++,.......,@,,,*:                           
     @++,,,+++++++++++++++++++++#++++++@8,++++++***#, ::*+,,,...,,,@,,,8.                           
     .@+,,,++++++++++++++++++++8++++++++@+,+++++***:@.88*+,,,,,,,,,@,,,@                            
      #*+,,,,+++++++++++++++++oo++++++++@:,,++++****@##,@,,,,,,,,,,@#,@@                            
       @++,,,,++++++++++++++++@*++++++++:@,,,++++***:@,++#+,,,,,,,,@@#o#o                           
       .@++,,,,,+++++++++++++*&*+++++++++@+,,,+++***:@,+++#,,,,,,,,@*@@#@+                          
        *#+++,,,.,+++++++++++8:*+++++++++@+,,,++++**:@:++++@,,,,,,,@*o#,,8o                         
         &8+++,,,,,,+++++++++#:*+++++++++@,,,,++++**o@@+++++@,,,,,+8**@,,,#.                        
          &8++++,,,,,,,+*++++#:**++++++++8#+,++****:@,.@++++oo,,,,@***:@,,o+                        
           o@+++++,,,,,,,,,++#:**+++++++++@+++++**:&@  @,++++@,,,,@*+**@,8@                         
            ,@*+++++,,,,,,,,,*o:**++++++++*@*+++**&@..o@+++++o:,,@*+++*o8,                          
              @&++++++,,,,,,,.#:::+++++++++:@@**:@@@@@&+,,,,,+@,o#*++++:&                           
               *@o++++++++,,,,@::::*+++++++++&@@@+@++++,,,,,,+@+@+++++**#                           
                 +@@#+++++++++:o::::***+++++++*@  #++++,,,,,,+#@:*++++**#                           
                     8@*+++++++@:::::**+++++++++8@@+++++,,,,,+8*:::**:*:#                           
                       ,@@:+++++#:::::*****++++++++++++++,,,++8:::::::::o                           
                          .&@@#:oo:::::******+++++++++++++++++@::::::::#                            
                               ,o@:::::::*****+*+++**+++++++++@o:::::::@                            
                                  ::::::::::*****:*****++++++*#ooo::::@+                            
                                   +o:::::::::::::::****+++++@ooooooo#@                             
                                     8::::::::::::::::******&#oooooo#@                              
                                      .&::::::::::::::::***o@ooooo&#8                               
                                       @:o::::::::::::::::#8oooo:*@*                                
                                       @:::::::::::::::::@:******@.                                 
                                       @::**++++****++++@*******@                                   
                                       @::**++++++++++:@******o@                                    
                                       @:***+++++++++@#******88                                     
                                       @:***++++++++@&:*****&#                                      
                                       @o:*+++++*:*@:*****o88.                                      
                                      @++,,,,,,,,,++,*8#:++*****#8.                                 
                                    ,@+,,,,,,,,,,,,,++++*&@:*****::8@.                              
                                    @++,,,,,,,,,,,,++++**8*.@8***oo@++@&                            
                                   @+++++++++++++++++:#:*8.  .@8@o#+,,,,@*                          
                                  .8++++++++++++++++**&@8#...  +@&@8++,,,:@                         
                                  #:*+++++++++++++++*#:  .#8,,  .@+,@o++,,,@.                       
                                  @::***************:@,..  *@.,  .@+,#@++,,,@.                      
                                  #::::::**********:::,...  *@..  .@,,#@+,,,+@                      
                                 .8:::::::::::::::::&+,,,,   &#,   .@,,#o+,,,+@                     
                                 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#  
```
---

## Installation and Usage of ASCII-ART

```console
$ git clone https://github.com/KhorSL/ASCII-ART.git
$ cd ASCII-ART
$ pip install -r requirements.txt
$ python ascii-art.py samples/images/dino.png
```

Artifacts generated will be in `output/`.

### Adjustments to Output Images

Adjust `FIXED_NEW_WDITH` and `large_font` to fine tune the image.

#### Example Adjustment
```python
''' other codes... '''

FIXED_NEW_WIDTH = 200

  ''' other codes... '''

def string_image(string, font_path=None):

  ''' other codes... '''
  large_font = 20  # get better resolution with larger size

  ''' other codes... '''
```

#### Example Result

![Clearer Dino](samples/images/dino_ascii_clearer.png)

---

## Future Plans
- No future plans as of now.

---

## References

- [Dinosaur Sprite](https://www.gameart2d.com/free-dino-sprites.html)
