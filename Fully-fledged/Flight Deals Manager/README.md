## Flight deals manager

A script which searches for best flight deals to requested cities on [**Kiwi.com**](https://www.kiwi.com/ "https://www.kiwi.com/"). It utilises Kiwi's [Tequila API](https://tequila.kiwi.com/ "https://tequila.kiwi.com/").

A script takes the data on desired destinations and highest price, which the user is ready to pay for the flight (or flights, if there are stopovers) from a previously established Google Sheet. It then tries to find valid IATA codes for the requested cities and, if successful, checks whether there are any flight connections on Kiwi, the total price of which is lower than the highest acceptable price entered by the user. Search results are saved in a JSON file. Starting location is hard-coded in main.py (default - Warsaw).
