import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_nollaa_varaston(self):
        varasto = Varasto(10, -10)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_tasoittaa_saldo_tilavuus(self):
        varasto = Varasto(10, 20)

        self.assertEqual(varasto.saldo, varasto.tilavuus)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_tilavuus_nollataan(self):
        varasto = Varasto(-10)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_ei_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ei_tilaa(self):
        varasto = Varasto(11, 10)
        varasto.lisaa_varastoon(2)

        self.assertAlmostEqual(varasto.saldo, varasto.tilavuus)

    def test_ottaa_liian_vahan(self):
        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_ota_kaikki_mita_voidaan(self):
        self.varasto.lisaa_varastoon(10)
        saatu_maara = self.varasto.ota_varastosta(20)

        self.assertAlmostEqual(saatu_maara, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_str_palautus(self):
        palautus = "saldo = 0, vielä tilaa 10"
        self.assertAlmostEqual(str(self.varasto), palautus)
