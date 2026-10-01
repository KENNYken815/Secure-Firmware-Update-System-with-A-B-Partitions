// Secure A/B firmware update reference implementation.
// Core policy: validate -> install inactive slot -> pending -> boot -> confirm -> activate/rollback.
#include <stdint.h>
typedef enum { SLOT_A=0, SLOT_B=1 } slot_t;
typedef struct { slot_t active,pending; uint32_t version,min_version,attempts; } boot_state_t;
void boot_init(boot_state_t*s,uint32_t min){s->active=SLOT_A;s->pending=SLOT_A;s->version=0;s->min_version=min;s->attempts=0;}
int install(boot_state_t*s,uint32_t version){if(version<s->min_version)return 0;s->pending=(s->active==SLOT_A)?SLOT_B:SLOT_A;s->version=version;s->attempts=0;return 1;}
slot_t boot_select(boot_state_t*s){if(s->pending!=s->active&&s->attempts<3){s->attempts++;return s->pending;}s->pending=s->active;s->attempts=0;return s->active;}
void confirm(boot_state_t*s){if(s->pending!=s->active){s->active=s->pending;s->min_version=s->version;s->attempts=0;}}
