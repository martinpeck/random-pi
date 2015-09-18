import mcpi.minecraft as minecraft
import mcpi.block as block

def create_temple():
    
    floor()
    walls()
    doors()
    roof()

def floor():
    mc = minecraft.Minecraft.create()
    pp = mc.player.getTilePos()
    
    for x in range (pp.x - 3, pp.x + 4):
    	for z in range (pp.z - 3, pp.z + 4):
    	    
    	    mc.setBlock(x, pp.y - 1, z, block.STONE_BRICK)

def walls():
    mc = minecraft.Minecraft.create()
    pp = mc.player.getTilePos()
    
    for y in range (pp.y, pp.y + 5):

        # top wall
    	for x in range (pp.x - 3, pp.x + 4):    	    
    	    mc.setBlock(x, y, pp.z + 3, block.IRON_BLOCK)

        # back wall
    	for x in range (pp.x - 3, pp.x + 4):
    	    mc.setBlock(x, y, pp.z - 3, block.IRON_BLOCK)    		
    
        # side wall (left)
        for z in range (pp.z - 2, pp.z + 3):
            mc.setBlock(pp.x - 3, y, z, block.DIAMOND_BLOCK)
            
        # side wall (right)
        for z in range (pp.z - 2, pp.z + 3):
            mc.setBlock(pp.x + 3, y, z, block.DIAMOND_BLOCK)

def doors():
    mc = minecraft.Minecraft.create()
    pp = mc.player.getTilePos()
    
    mc.setBlock(pp.x + 3, pp.y, pp.z, block.AIR)
    mc.setBlock(pp.x + 3, pp.y + 1, pp.z, block.AIR)    

def roof():
    mc = minecraft.Minecraft.create()
    pp = mc.player.getTilePos()
    
    for t in range (0, 3):
	for x in range (pp.x - (3 - t), pp.x + (3 - t) + 1):
    	    for z in range (pp.z - (3 - t), pp.z + (3 - t) + 1):    	    
    	        mc.setBlock(x, pp.y + 5 + t, z, block.GOLD_BLOCK)
