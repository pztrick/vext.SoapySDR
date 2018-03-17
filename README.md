# vext.SoapySDR

Use SoapySDR in a virtualenv on Linux, Windows or OSX.

This project uses the [Vext](https://github.com/stuaxo/vext) library to include system Python packages in virtualenvs.

## Usage

```
pip install vext.SoapySDR
```

## Dependencies

You must first build `SoapySDR` on your machine.

Follow the instructions [here](https://github.com/pothosware/SoapySDR/wiki/BuildGuide).

You may also need to sym-link the `SoapySRD` from its default install path of `/usr/local/...` to `/usr/lib/...`:

```
sudo ln -svf /usr/local/lib/python3/dist-packages/SoapySDR.py /usr/lib/python3/dist-packages/
sudo ln -svf /usr/local/lib/python3/dist-packages/_SoapySDR.so /usr/lib/python3/dist-packages/
```