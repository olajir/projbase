class ArrayDef:
    """Definition for a slide image."""
    def __init__(self, nb_block_rows, nb_block_cols,
                 block_row_cc, block_col_cc, block0_ulc, block_def):
        """Init."""
        self.nb_block_rows = nb_block_rows
        self.nb_block_cols = nb_block_cols
        self.block_row_cc = block_row_cc
        self.block_col_cc = block_col_cc
        self.block0_ulc = block0_ulc
        self.block_def = block_def

class BlockDef:
    """Definition for a slide block."""
    def __init__(self, nb_rows, nb_cols, row_pitch, col_pitch, spot_r):
        """Init."""
        self.nb_rows = nb_rows
        self.nb_cols = nb_cols
        self.row_pitch = row_pitch
        self.col_pitch = col_pitch
        self.spot_r = spot_r
