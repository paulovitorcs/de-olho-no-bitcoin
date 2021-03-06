# Bitcoin Watcher - De Olho no Bitcoin

It watches Bitcoin [Foxbit Watcher API](https://watcher-docs.foxbit.com.br/) and notificates you throw [Pushover](https://pushover.net/) with current price and variation 

## Usage:
You can install Pushover app and subscribe into [this channel](https://pushover.net/subscribe/DeOlhonoBitcoin-whrxw9eaz7dtxb1) for current Bitcoin values in BRL for every 30 minutes

## Installation:
- Make sure you have [Python](https://www.python.org/) installed
- Run pip for third party package installation
```bash
python -m pip install -r requirements.txt
```
- Do not forget to set `PUSHOVER_TOKEN` and `PUSHOVER_USER` on `.env` file
- Run `run.py` file
```bash
python run.py
```
## Routines:
If you want to, you can set a optional routine with a interval. If enabled, you received a notification on the specified set time.
- Set `HAS_ROUTINE` as `True`
- Set `INTERVAL` with the interval minutes you desire
