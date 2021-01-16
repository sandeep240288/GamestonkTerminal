import config_bot as cfg
import argparse
from discovery import alpha_vantage_api
from discovery import yahoo_finance_api
from discovery import reddit_api


# -----------------------------------------------------------------------------------------------------------------------
def print_discovery():
    """ Print help """

    print("   help          show this fundamental analysis menu again")
    print("   q             quit this menu, and shows back to main menu")
    print("   quit          quit to abandon program")
    print("")
    print("   sectors       show sectors performance [Alpha Vantage]")
    print("   gainers       show latest top gainers [Yahoo Finance]")
    print("   watchlist     show other users watchlist [Reddit]")
    print("   popular       show popular tickers [Reddit]")
    print("")
    return


# ---------------------------------------------------- MENU ----------------------------------------------------
def disc_menu():

    # Add list of arguments that the discovery parser accepts
    disc_parser = argparse.ArgumentParser(prog='discovery', add_help=False)
    disc_parser.add_argument('cmd', choices=['help', 'q', 'quit',
                                             'sectors', 'gainers', 'watchlist', 'popular'])

    print_discovery()

    # Loop forever and ever
    while True:
        # Get input command from user
        as_input = input('> ')
        
        # Parse fundamental analysis command of the list of possible commands
        try:
            (ns_known_args, l_args) = disc_parser.parse_known_args(as_input.split())

        except SystemExit:
            print("The command selected doesn't exist\n")
            continue
            
        if ns_known_args.cmd == 'help':
            print_discovery()

        elif ns_known_args.cmd == 'q':
            # Just leave the DISC menu
            return False

        elif ns_known_args.cmd == 'quit':
            # Abandon the program
            return True
        
        # ------------------------------------------------ ALPHA VANTAGE -----------------------------------------------
        elif ns_known_args.cmd == 'sectors':
            alpha_vantage_api.sectors(l_args)
        
        # ------------------------------------------------ YAHOO FINANCE ------------------------------------------------
        elif ns_known_args.cmd == 'gainers':
            yahoo_finance_api.gainers(l_args)

        # ---------------------------------------------------- REDDIT ---------------------------------------------------
        elif ns_known_args.cmd == 'watchlist':
            reddit_api.watchlist(l_args)

        elif ns_known_args.cmd == 'popular':
            reddit_api.popular_tickers(l_args)

        # ------------------------------------------------------------------------------------------------------------
        else:
            print("Command not recognized!")