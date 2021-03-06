import talib as ta


class Indicators:
    def __init__(self, df):
        df = self.__gen_indicators(df=df)
        # self.df = self.__price_pattern(df=df)

    @staticmethod
    def __gen_indicators(df):
        ## Overlap Studies Functions
        df['UPPER'], df['MIDDLE'], df['LOWER'] = ta.BBANDS(df.Close, timeperiod=90, nbdevup=2, nbdevdn=2, matype=0)
        df['DEMA']         = ta.DEMA(df.Close, 90)
        df['EMA90']        = ta.EMA(df.Close, 90)
        df['HT_TRENDLINE'] = ta.HT_TRENDLINE(df.Close)
        df['MA90']         = ta.MA(df.Close, 90)
        df['MAMA'], df['FAMA'] = ta.MAMA(df.Close)
        df['MAVP']         = ta.MAVP(df.Close, df.EMA90)
        df['MIDPOINT']     = ta.MIDPOINT(df.Close, 90)
        df['MIDPRICE']     = ta.MIDPRICE(df.High, df.Low, 90)
        df['SAR']          = ta.SAR(df.High, df.Low, acceleration=0, maximum=0)
        df['SAREXT']       = ta.SAREXT(df.High, df.Low, 0, 0, 0)
        df['SMA']          = ta.SMA(df.Close, 90)
        df['T3']           = ta.T3(df.Close, 90)
        df['TEMA']         = ta.TEMA(df.Close, 90)
        df['TRIMA']        = ta.TRIMA(df.Close, 90)
        df['WMA']          = ta.WMA(df.Close, 90)

        ## Momentum Indicator Funnctions
        df['ADX']          = ta.ADX(df.High, df.Low, df.Close, 90)
        df['ADXR']         = ta.ADXR(df.High, df.Low, df.Close, 90)
        df['APO']          = ta.APO(df.Close, 30, 90)
        df['AROONDOWN'], df['ARRONUP'] = ta.AROON(df.High, df.Low, 90)
        df['AROONOSC']     = ta.AROONOSC(df.High, df.Low, 90)
        df['BOP']          = ta.BOP(df.Open, df.High, df.Low, df.Close)
        df['CCI']          = ta.CCI(df.High, df.Low, df.Close, 90)
        df['CMO']          = ta.CMO(df.Close, 90)
        df['DX']           = ta.DX(df.High, df.Low, df.Close, 90)
        df['MACD'], df['MACDSIGNAL'], df['MACDHIST'] = ta.MACD(df.Close, fastperiod=12, slowperiod=26, signalperiod=9)
        df['MACDX'], df['MACDSIGNALX'], df['MACDHISTX'] = ta.MACDEXT(df.Close, fastperiod=12, slowperiod=26, signalperiod=9)
        df['MACDFIX'], df['MACDSIGNALFIX'], df['MACDHISTFIX'] = ta.MACDFIX(df.Close, 90)
        df['MFI']          = ta.MFI(df.High, df.Low, df.Close, df.Volume, 90)
        df['MINUS_DI']     = ta.MINUS_DI(df.High, df.Low, df.Close, 90)
        df['MINUS_DM']     = ta.MINUS_DM(df.High, df.Low, 90)
        df['MOM']          = ta.MOM(df.Close, 90)
        df['PLUS_DI']      = ta.PLUS_DI(df.High, df.Low, df.Close, 90)
        df['PLUS_DM']      = ta.PLUS_DM(df.High, df.Low, 90)
        df['PPO']          = ta.PPO(df.Close, 30, 90)
        df['ROC']          = ta.ROC(df.Close, 90)
        df['ROCR']         = ta.ROCR(df.Close, 90)
        df['ROCR100']      = ta.ROCR100(df.Close, 90)
        df['RSI']          = ta.RSI(df.Close,90)
        df['SLOWK'], df['SLOWD'] = ta.STOCH(df.High, df.Low, df.Close)
        df['FASTK'], df['FASTD'] = ta.STOCHF(df.High, df.Low, df.Close)
        df['FASTK_RSI'], df['FASTD_RSI'] = ta.STOCHRSI(df.Close, 90)
        df['TRIX']         = ta.TRIX(df.Close, 90)
        df['ULTOSC']       = ta.ULTOSC(df.High, df.Low, df.Close)
        df['WILLR']        = ta.WILLR(df.High, df.Low, df.Close, 90)

        ## Volume Indicator Functions
        df['AD']           = ta.AD(df.High, df.Low, df.Close, df.Volume)
        df['ADOSC']        = ta.ADOSC(df.High, df.Low, df.Close, df.Volume)
        df['OBV']          = ta.OBV(df.Close, df.Volume)

        ## Volatility Indicator Functions
        df['ATR']          = ta.ATR(df.High, df.Low, df.Close, 90)
        df['NATR']         = ta.NATR(df.High, df.Low, df.Close, 90)
        df['TRANGE']       = ta.TRANGE(df.High, df.Low, df.Close)

        ## Price Transform Functions
        df['AVGPRICE']     = ta.AVGPRICE(df.Open, df.High, df.Low, df.Close)
        df['MEDPRICE']     = ta.MEDPRICE(df.High, df.Low)
        df['TYPPRICE']     = ta.TYPPRICE(df.High, df.Low, df.Close)
        df['WCLPRICE']     = ta.WCLPRICE(df.High, df.Low, df.Close)

        ## Cycle Indicator Functions
        df['HT_DCPERIOD']  = ta.HT_DCPERIOD(df.Close)
        df['HT_DCPHASE']   = ta.HT_DCPHASE(df.Close)
        df['INPHASE'], df['QUADRATURE'] = ta.HT_PHASOR(df.Close)
        df['SINE'] , df['LEADSINE'] = ta.HT_SINE(df.Close)
        df['HT_TRENDMODE'] = ta.HT_TRENDMODE(df.Close)

        ## Beta
        df['BETA']         = ta.BETA(df.High, df.Low, 90)
        df['CORREL']       = ta.CORREL(df.High, df.Low, 90)
        df['LINEARREG']    = ta.LINEARREG(df.Close, 90)
        df['LINEARREG_ANGLE'] = ta.LINEARREG_ANGLE(df.Close, 90)
        df['LINEARREG_INTERCEPT'] = ta.LINEARREG_INTERCEPT(df.Close, 90)
        df['LINEARREG_SLOPE'] = ta.LINEARREG_SLOPE(df.Close, 90)
        df['STDDEV']       = ta.STDDEV(df.Close, 90, 1)
        df['TSF']          = ta.TSF(df.Close, 90)
        df['VAR']          = ta.VAR(df.Close, 90, 1)

        ## Math Transform Functions
        df['ACOS']         = ta.ACOS(df.Close)
        df['ASIN']         = ta.ASIN(df.Close)
        df['ATAN']         = ta.ATAN(df.Close)
        df['CEIL']         = ta.CEIL(df.Close)
        df['COS']          = ta.COS(df.Close)
        df['COSH']         = ta.COSH(df.Close)
        df['EXP']          = ta.EXP(df.Close)
        df['FLOOR']        = ta.FLOOR(df.Close)
        df['LN']           = ta.LN(df.Close)  # Log
        df['LOG10']        = ta.LOG10(df.Close)  # Log
        df['SIN']          = ta.SIN(df.Close)
        df['SINH']         = ta.SINH(df.Close)
        df['SQRT']         = ta.SQRT(df.Close)
        df['TAN']          = ta.TAN(df.Close)
        df['TANH']         = ta.TANH(df.Close)

        ## Math Operator Functions
        df['ADD']          = ta.ADD(df.High, df.Low)
        df['DIV']          = ta.DIV(df.High, df.Low)
        df['MAX']          = ta.MAX(df.Close, 90)
        df['MAXINDEX']     = ta.MAXINDEX(df.Close, 90)
        df['MIN']          = ta.MIN(df.Close, 90)
        df['MININDEX']     = ta.MININDEX(df.Close, 90)
        # df['MINMAX']       = ta.MINMAX(df.Close, 90)
        df['MINIDX'], df['MAXIDX'] = ta.MINMAXINDEX(df.Close, 90)
        df['MULT']         = ta.MULT(df.High, df.Low)
        df['SUB']          = ta.SUB(df.High, df.Low)
        df['SUM']          = ta.SUM(df.Close, 90)
        return df

    @staticmethod
    def __price_pattern(df):
        df['2CROWS'] = ta.CDL2CROWS(df.Open, df.High, df.Low, df.Close)
        df['3BLACKCROWS'] = ta.CDL3BLACKCROWS(df.Open, df.High, df.Low, df.Close)
        df['3INSIDE'] = ta.CDL3INSIDE(df.Open, df.High, df.Low, df.Close)
        df['3LINESTRIKE'] = ta.CDL3LINESTRIKE(df.Open, df.High, df.Low, df.Close)
        df['3OUTSIDE'] = ta.CDL3OUTSIDE(df.Open, df.High, df.Low, df.Close)
        df['STARSINSOUTH'] = ta.CDL3STARSINSOUTH(df.Open, df.High, df.Low, df.Close)
        df['3WHITESOLDIERS'] = ta.CDL3WHITESOLDIERS(df.Open, df.High, df.Low, df.Close)
        df['ABANDONED'] = ta.CDLABANDONEDBABY(df.Open, df.High, df.Low, df.Close)
        df['ADVBLOCK'] = ta.CDLADVANCEBLOCK(df.Open, df.High, df.Low, df.Close)
        df['BELTHOLD'] = ta.CDLBELTHOLD(df.Open, df.High, df.Low, df.Close)
        df['BREAKAWAY'] = ta.CDLBREAKAWAY(df.Open, df.High, df.Low, df.Close)
        df['CLOSING_MARU'] = ta.CDLCLOSINGMARUBOZU(df.Open, df.High, df.Low, df.Close)
        df['CONCEALING_BS'] = ta.CDLCONCEALBABYSWALL(df.Open, df.High, df.Low, df.Close)
        df['COUNTERATTACK'] = ta.CDLCOUNTERATTACK(df.Open, df.High, df.Low, df.Close)
        df['DARKCLOUD'] = ta.CDLDARKCLOUDCOVER(df.Open, df.High, df.Low, df.Close)
        df['DOJI'] = ta.CDLDOJI(df.Open, df.High, df.Low, df.Close)
        df['DOJISTAR'] = ta.CDLDOJISTAR(df.Open, df.High, df.Low, df.Close)
        df['DRAGONFLY'] = ta.CDLDRAGONFLYDOJI(df.Open, df.High, df.Low, df.Close)
        df['ENGULFING'] = ta.CDLENGULFING(df.Open, df.High, df.Low, df.Close)
        df['EVENING_DOJI'] = ta.CDLDOJISTAR(df.Open, df.High, df.Low, df.Close)
        df['EVENING_STAR'] = ta.CDLEVENINGSTAR(df.Open, df.High, df.Low, df.Close)
        df['GAPSIDEWHITE'] = ta.CDLGAPSIDESIDEWHITE(df.Open, df.High, df.Low, df.Close)
        df['GRAVESTONE_DOJI'] = ta.CDLGRAVESTONEDOJI(df.Open, df.High, df.Low, df.Close)
        df['HAMMER'] = ta.CDLHAMMER(df.Open, df.High, df.Low, df.Close)
        df['HANGINGMAN'] = ta.CDLHANGINGMAN(df.Open, df.High, df.Low, df.Close)
        df['HARAMI'] = ta.CDLHARAMI(df.Open, df.High, df.Low, df.Close)
        df['HARAMICROSS'] = ta.CDLHARAMICROSS(df.Open, df.High, df.Low, df.Close)
        df['HIGHWAVE'] = ta.CDLHIGHWAVE(df.Open, df.High, df.Low, df.Close)
        df['HIKKAKE'] = ta.CDLHIKKAKE(df.Open, df.High, df.Low, df.Close)
        df['HIKAKEMOD'] = ta.CDLHIKKAKEMOD(df.Open, df.High, df.Low, df.Close)
        df['HOMING_PEGION'] = ta.CDLHOMINGPIGEON(df.Open, df.High, df.Low, df.Close)
        df['IDENTICAL3CROWS'] = ta.CDLIDENTICAL3CROWS(df.Open, df.High, df.Low, df.Close)
        df['INNECK'] = ta.CDLINNECK(df.Open, df.High, df.Low, df.Close)
        df['INVERTHAMMER'] = ta.CDLINVERTEDHAMMER(df.Open, df.High, df.Low, df.Close)
        df['KICKING'] = ta.CDLKICKING(df.Open, df.High, df.Low, df.Close)
        df['KICKBYLENGTH'] = ta.CDLKICKINGBYLENGTH(df.Open, df.High, df.Low, df.Close)
        df['LADDER_BOTTOM'] = ta.CDLLADDERBOTTOM(df.Open, df.High, df.Low, df.Close)
        df['LONGLEG_DOJI'] = ta.CDLLONGLEGGEDDOJI(df.Open, df.High, df.Low, df.Close)
        df['LONGLINE_CANDLE'] = ta.CDLLONGLINE(df.Open, df.High, df.Low, df.Close)
        df['MARUBOZU'] = ta.CDLMARUBOZU(df.Open, df.High, df.Low, df.Close)
        df['MATCHINGLOW'] = ta.CDLMATCHINGLOW(df.Open, df.High, df.Low, df.Close)
        df['MATHOLD'] = ta.CDLMATHOLD(df.Open, df.High, df.Low, df.Close)
        df['MORNING_DOJI'] = ta.CDLMORNINGDOJISTAR(df.Open, df.High, df.Low, df.Close)
        df['MORNINGSTAR'] = ta.CDLMORNINGSTAR(df.Open, df.High, df.Low, df.Close)
        df['ONNECK'] = ta.CDLONNECK(df.Open, df.High, df.Low, df.Close)
        df['PIERCING'] = ta.CDLPIERCING(df.Open, df.High, df.Low, df.Close)
        df['RICKSHAW'] = ta.CDLRICKSHAWMAN(df.Open, df.High, df.Low, df.Close)
        df['RISEFALL3M'] = ta.CDLRISEFALL3METHODS(df.Open, df.High, df.Low, df.Close)
        df['SEPARATING'] = ta.CDLSEPARATINGLINES(df.Open, df.High, df.Low, df.Close)
        df['SHOOTING_STAR'] = ta.CDLSHOOTINGSTAR(df.Open, df.High, df.Low, df.Close)
        df['SHORTLINE'] = ta.CDLSHORTLINE(df.Open, df.High, df.Low, df.Close)
        df['SPINNINGTOP'] = ta.CDLSPINNINGTOP(df.Open, df.High, df.Low, df.Close)
        df['STALLED'] = ta.CDLSTALLEDPATTERN(df.Open, df.High, df.Low, df.Close)
        df['STICK_SAND'] = ta.CDLSTICKSANDWICH(df.Open, df.High, df.Low, df.Close)
        df['TAKURI'] = ta.CDLTAKURI(df.Open, df.High, df.Low, df.Close)
        df['TASUKIGAP'] = ta.CDLTASUKIGAP(df.Open, df.High, df.Low, df.Close)
        df['THRUSTING'] = ta.CDLTHRUSTING(df.Open, df.High, df.Low, df.Close)
        df['TRISTAR'] = ta.CDLTRISTAR(df.Open, df.High, df.Low, df.Close)
        df['UNIQUE3RIVER'] = ta.CDLUNIQUE3RIVER(df.Open, df.High, df.Low, df.Close)
        df['UPGAP2CROWS'] = ta.CDLUPSIDEGAP2CROWS(df.Open, df.High, df.Low, df.Close)
        df['UPGAP3METHODS'] = ta.CDLXSIDEGAP3METHODS(df.Open, df.High, df.Low, df.Close)
        return df