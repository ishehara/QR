FROM python

WORKDIR /usr/src/app/

RUN pip install qrcode

COPY qr1.py $WORKDIR
COPY qr2.py $WORKDIR
COPY readqr.py $WORKDIR

CMD [ "python","./qr1.py","./qr2.py","./readqr.py"]