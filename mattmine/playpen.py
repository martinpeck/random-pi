import minecraft as minecraft
import block as block

mc = minecraft.Minecraft.create()

def Chimney(id):
	pp = mc.player.getTilePos()

	for i in range (pp.y, pp.y+10):
		mc.setBlock(pp.x + 1, i, pp.z, id)
		mc.setBlock(pp.x + 1, i, pp.z -1, id)
		mc.setBlock(pp.x + 1, i, pp.z +1, id)
 
		mc.setBlock(pp.x - 1, i, pp.z, id)
		mc.setBlock(pp.x - 1, i, pp.z -1, id)
		mc.setBlock(pp.x - 1, i, pp.z +1, id)
		
		mc.setBlock(pp.x , i, pp.z -1, id)
		mc.setBlock(pp.x , i, pp.z +1, id)
	

def StripyChimney():
	pp = mc.player.getTilePos()

	for i in range (pp.y-50, pp.y+50):

		if i % 2 == 0:
			id = block.FARMLAND



		else:
			id = block.DIAMOND_BLOCK

		mc.setBlock(pp.x + 1, i, pp.z, id)
		mc.setBlock(pp.x + 1, i, pp.z -1, id)
		mc.setBlock(pp.x + 1, i, pp.z +1, id)
 
		mc.setBlock(pp.x - 1, i, pp.z, id)
		mc.setBlock(pp.x - 1, i, pp.z -1, id)
		mc.setBlock(pp.x - 1, i, pp.z +1, id)
		
		mc.setBlock(pp.x , i, pp.z -1, id)
		mc.setBlock(pp.x , i, pp.z +1, id)

		mc.setBlock(pp.x , i, pp.z, block.AIR)

