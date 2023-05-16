#include <stdio.h>
#include <unistd.h>
#include <stdint.h>
#include <string.h>
#include <signal.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>

// gcc ancient_interface.c -lrt -no-pie -s -o ancient_interface

#define USER        "user"
#define HOSTNAME    "host"

#define PROMPT (USER "@" HOSTNAME "$ ")

#define ALARM_HIT   "Alarm has been hit!\n"

#define ALARM_HELP  "alarm <seconds>\n"
#define ECHO_HELP   "echo <$variable/string>\n"
#define READ_HELP   "read <amount of bytes> <variable>\n"

#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof(arr[0]))

struct commands {
    const char *s;
    int (*func)();
};

struct kv {
    char *key;
    char *val;
};

struct variables {
    int32_t size;
    struct kv *kv;
};

int cmd_exit(char *params);
int cmd_alarm(char *params);
int cmd_echo(char *params);
int cmd_read(char *params);
int cmd_whoami(char *params);
int cmd_vars(char *params);

static const struct commands CMDS[] = {
    {   "exit",     &cmd_exit   },
    {   "alarm",    &cmd_alarm  },
    {   "echo",     &cmd_echo   },
    {   "read",     &cmd_read   },
    {   "whoami",   &cmd_whoami },
    {   "vars",     &cmd_vars   },
};

static struct variables VARS;

void alarm_handler()
{
    write(1, ALARM_HIT, sizeof(ALARM_HIT));
}

void setup()
{
    struct sigaction sa;

    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    VARS.size = 64;
    VARS.kv = calloc(VARS.size, sizeof(struct kv));
    if (VARS.kv == NULL)
    {
        perror("calloc");
        exit(EXIT_FAILURE);
    }

    sa.sa_flags = 0;
    sa.sa_sigaction = &alarm_handler;
    if (sigaction(SIGALRM, &sa, NULL) < 0)
    {
        perror("sigaction");
        exit(EXIT_FAILURE);
    }
}

char *get_var(char *var)
{
    char *p = NULL;

    for (int32_t i = 0; i < VARS.size; i++)
    {
        if (VARS.kv[i].key == NULL)
            continue;

        if (strcmp(var, VARS.kv[i].key) == 0)
        {
            p = VARS.kv[i].val;
            break;
        }
    }

    return p;
}

int put_var(char *key, char *val)
{
    int32_t idx;

    idx = -1;
    for (int32_t i = 0; i < VARS.size; i++)
    {
        if (VARS.kv[i].key == NULL)
        {
            idx = i;
            break;
        }
    }

    if (idx < 0)
        return 1;

    VARS.kv[idx].key = strdup(key);
    VARS.kv[idx].val = strdup(val);

    if (VARS.kv[idx].key == NULL || VARS.kv[idx].val == NULL)
        return 1;

    return 0;
}

int cmd_exit(char *params)
{
    for (int32_t i = 0; i < VARS.size; i++)
    {
        if (VARS.kv[i].key != NULL)
            free(VARS.kv[i].key);
        if (VARS.kv[i].val != NULL)
            free(VARS.kv[i].val);
    }

    exit(EXIT_SUCCESS);
}

int cmd_alarm(char *params)
{
    int32_t seconds;
    struct sigevent sev;
    struct itimerspec its;
    static timer_t tmid;

    if (params == NULL)
    {
        printf(ALARM_HELP);
        return 1;
    }

    seconds = atoi(params);
    if (seconds <= 0)
        return 1;

    sev.sigev_notify = SIGEV_SIGNAL;
    sev.sigev_signo = SIGALRM;

    if (timer_create(CLOCK_REALTIME, &sev, &tmid) < 0)
    {
        perror("timer_create");
        return 1;
    }

    its.it_value.tv_sec = seconds;
    its.it_value.tv_nsec = 0;
    its.it_interval.tv_sec = 0;
    its.it_interval.tv_nsec = 0;

    if (timer_settime(tmid, 0, &its, NULL) < 0)
    {
        perror("timer_settime");
        return 1;
    }

    return 0;
}

int cmd_echo(char *params)
{
    int32_t found;
    char *val;

    if (params == NULL)
    {
        printf(ECHO_HELP);
        return 1;
    }

    if (*params == '$')
    {
        val = get_var(params + 1);

        if (val == NULL)
            printf("%s is not defined\n", params);
        else
            printf("%s\n", val);
    }
    else
    {
        printf("%s\n", params);
    }
    
    return 0;
}

int cmd_read(char *params)
{
    char buf[4096] = { 0 };
    char *p;
    int32_t ret;
    int32_t read_bytes;
    uint32_t amnt;

    if (params == NULL)
    {
        printf(READ_HELP);
        return 1;
    }

    p = strchr(params, ' ');
    if (p == NULL)
    {
        printf(READ_HELP);
        return 1;
    }

    *p = '\0';

    if (get_var(p + 1) != NULL)
    {
        printf("read: variable $%s already exists\n", p + 1);
        return 1;
    }

    amnt = atoi(params);
    if (amnt == 0 || amnt >= sizeof(buf))
    {
        printf("read: invalid size\n");
        return 1;
    }

    read_bytes = 0;
    do
    {
        read_bytes += read(0, buf + read_bytes, amnt - read_bytes);
    } while (read_bytes != amnt);

    getchar();
    
    if (put_var(p + 1, buf) != 0)
        printf("read: maximum amount of variables reached\n");

    return 0;
}

int cmd_whoami(char *params)
{
    printf("%s\n", USER);

    return 0;
}

int cmd_vars(char *params)
{
    for (int32_t i = 0; i < VARS.size; i++)
    {
        if (VARS.kv[i].key != NULL)
        {
            printf("%s\n", VARS.kv[i].key);
        }
    }

    return 0;
}

int main()
{
    char buf[4096];
    char *p;
    char *params;
    int32_t ret;
    int32_t found;

    setup();

    while (1)
    {
        printf(PROMPT);

        memset(buf, '\0', sizeof(buf));

        ret = read(0, buf, sizeof(buf) - 1);
        if (ret <= 1)
            continue;

        buf[ret - 1] = '\0';

        p = strchr(buf, ' ');
        if (p != NULL)
        {
            *p++ = '\0';

            while (*p == ' ')
                p++;
                
            params = p;
        }
        else
        {
            params = NULL;
        }

        found = 0;
        for (int32_t i = 0; i < ARRAY_SIZE(CMDS); i++)
        {
            if (strcmp(buf, CMDS[i].s) == 0)
            {
                found = 1;
                CMDS[i].func(params);
                break;
            }
        }

        if (!found)
            printf("%s: command not found\n", buf);
    }

    return 0;
}
