# listen2me
Here is a repo for English-learner on listen

# [Project Disclaimer](Statement.md)
**Please must read it!**

# How to use
## git this repo and make your env

```bash
git clone https://github.com/sepinetam/listen2me.git
```

```bash
cd listen2me
python -m venv venv
source venv/bin/activate
```

## Set your config
If you want use default config, you just rename the file `_config.demo.py` to `_config.py`

### config parm explain
If you want to custom your config, you also should do the rename part.

| parm           | description                                      |
|----------------|--------------------------------------------------|
| SRC_BASE       | source dir                                       |
| WORDS_BASE     | your word list file('.txt', '.csv', '.json')     |
| pron_loca      | pronunciation location('uk', 'us')               |
| is_play        | whether play the voice while download mp3        |
| is_check       | whether show the word while play(the learn part) |
| check_position | when to check                                    |
| self_destruct  | `rm -rf` SRC_BASE                                |

## run it
if you do everything, just run it!
```bash
pyhton run.py
```

# TODO
- [x] Set up the project structure
- [x] Implement basic web scraping functionality
- [ ] Add error handling and logging
- [x] Write unit tests
- [ ] Create detailed documentation
- [ ] Optimize the scraper for performance
- [ ] Add support for more dictionaries
