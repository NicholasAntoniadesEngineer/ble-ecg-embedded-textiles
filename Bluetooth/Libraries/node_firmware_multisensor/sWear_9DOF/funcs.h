#ifndef funcs_h
#define funcs_h

#define CHIPID 2

#define LEDblink() { U2TXREG=0xfc; U2TXREG=0xfc; U2TXREG=0xfc; }

#define msleep longWait

void longWait();

void setupPIC();
void ProcessIO();
void debugTX(unsigned char v);

void queueIMUasBase64(void);

void setOffsets();
void updateIMU(void);
void accSend(void);
void reqFrame(void);


int getFlag(char flag);
void setFlag(char flag);
void clearFlag(char flag);
 
void doContinuousRead();


#endif
