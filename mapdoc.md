Map Coordinate States

+-----------+-------+-------------------------------------------------------------------------+
| 0         | empty | an empty field on the map                                               |
| 1         | bomb  | a bomb that explodes on the next turn and kills players in radius       |
| 2         | wall  | will block bombs and players                                            |
| [0-9]{6}  | user  | the user placed itself on the map. he's representing himself via his ID |
+-----------+-------+-------------------------------------------------------------------------+
