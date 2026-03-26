##########################################################################
#
#  THIS FILE IS GENERATED FROM TEMPLATE. DON'T MODIFY IT
#
#  uniee_values.py
#
#  Created on: Jan 14, 2022
#      Author: Miroslav Ondra <ondra@faster.cz>
# 


class Product:
	def __init__(self, id, name, **kwargs):
		self.id = id
		self.name = name
		self.vars = kwargs

class Board:
	def __init__(self, id, name, slots, **kwargs):
		self.id = id
		self.name = name
		self.slots = slots
		self.vars = kwargs

class Slot:
	def __init__(self, slot, **kwargs):
		self.slot = slot
		self.vars = kwargs

products = {
  '774': Product(774, 'E410', dt='unipi_e410' , udev='e410' ),
  '1030': Product(1030, 'E411', dt='unipi_e411' , udev='e411' ),
  '1286': Product(1286, 'E412', dt='unipi_e412' , udev='e412' ),
  '1542': Product(1542, 'E413', dt='unipi_e413' , udev='e413' ),
  '1798': Product(1798, 'E414', dt='unipi_e414' , udev='e414' ),
  '2054': Product(2054, 'E415', dt='unipi_e415' , udev='e415' ),
}

boards = {
  '201': Board(201, 'UDELAB01',{
    }, has_watchdog1='1' , has_lte='1' , has_tpm='1' ),
  '202': Board(202, 'UDELAB02',{
    }, has_watchdog1='1' , has_tpm='1' ),
  '203': Board(203, 'UDELAB03',{
    }, has_watchdog1='1' , has_lte='1' , has_tpm='1' ),
  '204': Board(204, 'UDELAB04',{
    }, has_watchdog1='1' , has_lte='1' , has_tpm='1' ),
  '205': Board(205, 'UDELAB05',{
    }, has_watchdog1='1' , has_tpm='1' ),
  '206': Board(206, 'UDELAB06',{
    }, has_watchdog1='1' , has_tpm='1' ),
}

# Family names
family = {
  '1': 'UNIPI1',
  '2': 'G1XX',
  '3': 'NEURON',
  '5': 'AXON',
  '6': 'EDGE',
  '7': 'PATRON',
  '15': 'IRIS',
  '16': 'OEM',
}

def unipi_product_info(product_id, version=None):
	''' return product_info or none '''
	return products.get(str(product_id), None)

def unipi_product_info_by_name(product_name, version=None):
	''' return product_info or none '''
	for k,v in products.items():
		if v.name.lower() == product_name.lower(): 
			return v
		if v.name.lower() == product_name.lower().replace('-','_'):
			return v
	short_name = product_name.lower()
	compare_len = len(short_name) - 1;
	while compare_len > 3:
		for k,v in products.items():
			if v.name.lower()[:compare_len] == short_name[:compare_len]: 
				return v
		compare_len -= 1

	return None

def unipi_board_info(board_id, slot=None, version=None):
	''' return board_info or None '''
	board_info = boards.get(str(board_id), None)
	if slot == None or board_info == None:
		return board_info
	if board_info.slots is None:
		return None
	return board_info.slots.get(str(slot), None)


def unipi_family_name(product_id):
	''' return family name or none '''
	return family.get(str(product_id & 0xff), None)
