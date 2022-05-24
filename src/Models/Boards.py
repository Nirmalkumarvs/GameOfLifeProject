#to create specified active cell pattern in the board
from src.Models.Boards import *
from src.Models.BoardsContainer import KickbackPattern,Acorn,BlinkerPattern,SquarePattern,ToadPattern,TrianglePattern,Tpattern,TwoGliderPattern

AVAILABLE_BOARDS={1:["Kickback",KickbackPattern.KickBackPattern()],2:["TwoGlider",TwoGliderPattern.TwoGliderPattern()],3:["Acorn",Acorn.Acorn()],4:["T-pattern",Tpattern.Tpattern()],5:["Square",SquarePattern.SquarePattern()],6:["Triangle",TrianglePattern.TrianglePattern()],7:["Blinker",BlinkerPattern.BlinkerPattern()],8:["Toad",ToadPattern.ToadPattern()]}

