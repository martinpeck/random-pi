import mcpi.minecraft as mine
import mcpi.block as block

# makes the player appear ypos blocks above the ground
def test_a(ypos):
    
    # create the minecraft object
    mo = mine.Minecraft.create()

    # this one gets the player object
    me = mo.player

    # this gets the players position
    pos = me.getPos()

    # this sets your position
    me.setPos(pos.x,ypos,pos.z)

# moves the player to the middle of the map
def test_b():

    mo = mine.Minecraft.create()
    me = mo.player

    pos = me.getPos()
    me.setPos(0.0,0.0,0.0)


def test_c():

    mo = mine.Minecraft.create()

    mo.setBlock(0,0,0,1)
    mo.setBlock(0,1,0,block.STONE)

    mo.setBlock(0,2,0,block.GOLD_BLOCK)
    mo.setBlock(0,1,1,block.LAPIS_LAZULI_BLOCK)
    mo.setBlock(0,1,-1,block.SANDSTONE)
    mo.setBlock(1,1,0,block.LEAVES)
    mo.setBlock(-1,1,0,block.WOOD)

def test_d():

    mo = mine.Minecraft.create()

    mo.setBlock(0,0,0,0)
    mo.setBlock(0,1,0,block.AIR)

    mo.setBlock(0,2,0,block.AIR)
    mo.setBlock(0,1,1,block.AIR)
    mo.setBlock(0,1,-1,block.AIR)
    mo.setBlock(1,1,0,block.AIR)
    mo.setBlock(-1,1,0,block.AIR)

def test_e():
    
    mo = mine.Minecraft.create()
    me = mo.player

    pos = me.getPos()
    print pos

    tilepos = me.getTilePos()
    print tilepos
    

def test_f():
    
    mo = mine.Minecraft.create()
    me = mo.player

    tilepos = me.getTilePos()

    mo.setBlock(tilepos.x, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)

def test_g():
    
    mo = mine.Minecraft.create()
    me = mo.player

    tilepos = me.getTilePos()

    mo.setBlock(tilepos.x, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)
    mo.setBlock(tilepos.x + 1, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)
    mo.setBlock(tilepos.x + 2, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)
    mo.setBlock(tilepos.x + 3, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)
    mo.setBlock(tilepos.x + 4, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)
    mo.setBlock(tilepos.x + 5, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)
    mo.setBlock(tilepos.x + 6, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)
    mo.setBlock(tilepos.x + 7, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)
    mo.setBlock(tilepos.x + 8, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)
    mo.setBlock(tilepos.x + 9, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)

def test_loop(start,finish):

    for i in range(start,finish):
        print i



def test_h(length):
    
    mo = mine.Minecraft.create()
    me = mo.player

    tilepos = me.getTilePos()

    for i in range(0,length):
        mo.setBlock(tilepos.x + i, tilepos.y - 1,tilepos.z,block.DIAMOND_BLOCK)

def test_below():
    mo = mine.Minecraft.create()
    me = mo.player

    tilepos = me.getTilePos()

    b = mo.getBlock(tilepos.x, tilepos.y -1, tilepos.z)

    print b

def test_i(newblock):
    mo = mine.Minecraft.create()
    me = mo.player

    tilepos = me.getTilePos()

    flag = True
    y_diff = 1

    while flag:
        b = mo.getBlock(tilepos.x, tilepos.y - y_diff, tilepos.z)
        if b == block.AIR:
            mo.setBlock(tilepos.x, tilepos.y - y_diff, tilepos.z,newblock)
            y_diff = y_diff + 1
        else:
            flag = False


def build_wall(length,height,block):
    mo = mine.Minecraft.create()
    me = mo.player

    tilepos = me.getTilePos()

    for y in range(0,height):
        for z in range(0,length):
            mo.setBlock(tilepos.x+1,tilepos.y + y,tilepos.z + z,block)  
