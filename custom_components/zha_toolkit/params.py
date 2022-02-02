# Constants related to parameters


# Constants representing input parameter keys
class USER_PARAMS_consts:
    __slots__ = ()
    CMD = "cmd"
    ENDPOINT = "endpoint"
    CLUSTER = "cluster"
    ATTRIBUTE = "attribute"
    ATTR_TYPE = "attr_type"
    ATTR_VAL = "attr_val"
    CODE = "code"
    MIN_INTRVL = "min_interval"
    MAX_INTRVL = "max_interval"
    REPTBLE_CHG = "reportable_change"
    DIR = "dir"
    MANF = "manf"
    TRIES = "tries"
    EXPECT_REPLY = "expect_reply"
    ARGS = "args"
    STATE_ID = "state_id"
    STATE_ATTR = "state_attr"
    ALLOW_CREATE = "allow_create"
    EVENT_SUCCESS = "event_success"
    EVENT_FAIL = "event_fail"
    EVENT_DONE = "event_done"
    READ_BEFORE_WRITE = "read_before_write"
    READ_AFTER_WRITE = "read_after_write"
    WRITE_IF_EQUAL = "write_if_equal"
    OUTCSV = "csvout"
    CSVLABEL = "csvlabel"


USER_PARAMS = USER_PARAMS_consts()


# Constants representing internal parameters keys
class INTERNAL_PARAMS_consts:
    __slots__ = ()
    ALLOW_CREATE = "allow_create"
    ARGS = "args"
    ATTR_ID = "attr_id"
    ATTR_TYPE = "attr_type"
    ATTR_VAL = "attr_val"
    CLUSTER_ID = "cluster_id"
    CMD_ID = "cmd_id"
    CODE = "code"
    DIR = "dir"
    EP_ID = "endpoint_id"
    EVT_DONE = "event_done"
    EVT_FAIL = "event_fail"
    EVT_SUCCESS = "event_success"
    EXPECT_REPLY = "expect_reply"
    MANF = "manf"
    MAX_INTERVAL = "max_interval"
    MIN_INTERVAL = "min_interval"
    READ_AFTER_WRITE = "read_after_write"
    READ_BEFORE_WRITE = "read_before_write"
    REPORTABLE_CHANGE = "reportable_change"
    STATE_ATTR = "state_attr"
    STATE_ID = "state_id"
    TRIES = "tries"
    WRITE_IF_EQUAL = "write_if_equal"
    CSV_FILE = "csvfile"
    CSV_LABEL = "csvlabel"


INTERNAL_PARAMS = INTERNAL_PARAMS_consts()
