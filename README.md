# Brain-computer-interface

Brain Computer Interface(BCI) ­based  automatic control of recognition has  been  a very active 
research topic in recent years with motivating applications such as human  computer   interaction
(HCI),   electronics  device   control   and   home   appliances   control.  In   this   paper we
present   a   system   that   uses  the   kinect   for   detecting   user   who   will   control
the   home   appliances,   MATLAB   tool  processes   captured   image  by the kinect and detect
user   who   wore   RED   T­-shirt   then it finds   location   of   that user and relative angle
of each device with respect to the user and sent this relative angle to raspberry PI through wireless
UDP connection.Next BCI module which detects eye blink with help of the electroencephalographic (EEG)
signals.  These   signals   are   sent   through   a   Bluetooth  connection   to   a   PC   that   processes   it   in   real  time   and   the   blink   strength   is   sent   through  wireless   connection   to   a   Raspberry   PI.   Now,  user   has   android   application   which   gives  user’s   viewing   direction   at   a   given   time.   This  application   can   detect   angle   with   help   of  inbuilt   gyroscope   of   mobile   phone.   This  angle   is   also   sent   through   wireless   UDP  connection   to   a   Raspberry   PI.   Finally,  Raspberry   PI   compares   these   two   angles,  one   is sent   from   MATLAB   tool   and   another  is   sent   from   android   mobile   app   if   these   two  angle   matches   the   user   can   control   device  using eye blink.
