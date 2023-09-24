#   import dataGeneration as dg
import userInterface as ui
import logger as lg
import crud


# dg.start() 
lg.logging.info('Start')
crud.init_data_base('base_phone.csv')
ui.ls_menu()