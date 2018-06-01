const githubSettings = {
    docsRepo: 'axibase/axibase-collector',
    editLinks: true,
    editLinkText: 'Help us improve this page!'
};

const topNavMenu = [
    {
        text: 'Jobs',
        link: '/jobs',
        items: [
            {text: 'AWS', link: '/jobs/aws.md'},
            {text: 'Docker', link: '/jobs/docker.md'},
            {text: 'File', link: '/jobs/file.md'},
            {text: 'HTTP', link: '/jobs/http.md'},
            {text: 'ICMP', link: '/jobs/icmp.md'},
            {text: 'JDBC', link: '/jobs/jdbc.md'},
            {text: 'JMX', link: '/jobs/jmx.md'},
            {text: 'JSON', link: '/jobs/json.md'},
            {text: 'Kafka', link: '/jobs/kafka.md'},
            {text: 'OVPM', link: '/jobs/ovpm.md'},
            {text: 'PI', link: '/jobs/pi.md'},
            {text: 'SNMP', link: '/jobs/snmp.md'},
            {text: 'Socrata', link: '/jobs/socrata.md'},
            {text: 'TCP', link: '/jobs/tcp.md'}
        ],
        highlighted: true
    },
    {
        text: 'Data Sources', items: [
            {text: 'Database', link: '/jobs/jdbc-data-source.html'},
            {text: 'HTTP Pool', link: '/jobs/http-pool.md'},
            {text: 'Kafka Consumer', link: "/jobs/kafka-consumer.md"}
        ]
    },
    {text: 'Examples', link: '/jobs/examples/', highlighted: true},
];


const landingPageMenu = [
    '',
    {
        title: 'Installation', children: [
            ['/requirements.md', 'Requirements'],
            ['/installation.md', 'Host'],
            ['/installation-on-docker.md', 'Docker'],
            ['/installation-on-kubernetes.md', 'Kubernetes'],
            ['/configure-administrator-account.md', 'Administrator Account'],
            ['https://axibase.com/docs/atsd/administration/collector-account.html', 'Collector Account'],
            '/atsd-server-connection.md',
            ['/docker-bundle.md', 'ATSD and Collector Bundle'],
            '/installation-firefox-webdriver.md',
        ],
        collapsable: true
    },
    {
        title: 'Updating', children: [
            ['/updating-collector-on-docker.md', 'Host'],
            ['/updating-collector.md', 'Docker']
        ],
        collapsable: true
    },
    {
        title: 'Administration', children: [
            '/logging.md',
            '/monitoring.md'
        ],
        collapsable: true
    },

    {
        title: 'Job\'s Configuration', children: [

            ['/job-generic.md', 'Generic'],
            ['/job-autostart.md', 'Autostart'],
            '/scheduling.md'
        ],
        collapsable: true
    },
    {
        title: 'Automation', children: [
            '/collections.md',
            '/functions-freemarker.md',
        ],
        collapsable: true
    }
];

const administrationMenu = ['/monitoring.md', '/logging.md'];

const examplesMenu = [
    ['/jobs/examples/activemq/', 'ActiveMQ'],
    ['/jobs/examples/derby/', 'Derby Database'],
    {
        title: 'File', children: [
            '/jobs/examples/file/airnow/',
            '/jobs/examples/file/australia-bom/',
            '/jobs/examples/file/duckduckgo/',
            '/jobs/examples/file/energinet-ftp/',
            '/jobs/examples/file/nginx/',
            '/jobs/examples/file/noaa-mooring/',
            '/jobs/examples/file/pvout/',
            '/jobs/examples/file/ssn/',
            '/jobs/examples/file/stackoverflow/',
            '/jobs/examples/file/uk-caa/',
            '/jobs/examples/file/yahoo-finance/'
        ]
    },
    ['/jobs/examples/hp-openview/', 'HP OpenView'],
    ['/jobs/examples/jetty/', 'Jetty'],
    {
        title: 'JSON', children: [
            '/jobs/examples/json/bls/',
            '/jobs/examples/json/github-daily-summary/',
            '/jobs/examples/json/nginx-status/',
            '/jobs/examples/json/australia-weather/',
            '/jobs/examples/json/fields-with-non-alphanumeric/',
            '/jobs/examples/json/json_lines/'

        ]
    },
    ['/jobs/examples/jvm/', 'JVM'],
    ['/jobs/examples/mysql/', 'MySQL'],
    ['/jobs/examples/nginx/', 'nginx'],
    ['/jobs/examples/oracle-enterprise-manager/', 'Oracle EM'],
    {
        title: 'PI', children: [
            ['/jobs/examples/pi/export-metrics.html', 'Transform PI points to ATSD metrics'],
            ['/jobs/examples/pi/export-archive-data.html', 'Export PI archive data as ATSD series']
        ]
    },
    ['/jobs/examples/postgres/', 'PostgreSQL'],
    ['/jobs/examples/scom/', 'SCOM'],
    ['/jobs/examples/socrata/state-government.md', 'Socrata'],
    ['/jobs/examples/solarwinds/', 'SolarWinds'],
    ['/jobs/examples/tomcat/', 'Tomcat'],
    ['/jobs/examples/vmware/', 'VMware']

];


const dataSourcesMenu = [
    ['/jobs/jdbc-data-source.html', 'Database'],
    ['/jobs/http-pool.html', 'HTTP Pool'],
    ['/jobs/kafka-consumer.html', 'Kafka Consumer']
];

const confMenu = [
    {
        title: 'General', children: [
            ['/configure-administrator-account.md', 'Administrator Account'],
            ['/atsd-server-connection.md', 'ATSD Connection']
        ]
    },
    {
        title: 'Job', children: [
            ['/job-generic.md', 'Generic'],
            ['/job-autostart.md', 'Autostart'],
            ['/scheduling.md', 'Scheduling'],
        ]
    }
];

module.exports = {
    base: '/docs/axibase-collector/',
    title: 'Axibase Collector',
    description: "User manual and API reference for Axibase® Time Series Database",
    head: [
        ['link', {rel: 'shortcut icon', href: '/favicon.ico'}]
    ],
    staticFilesExtensionsTest: /(?:tcollector|\.(?:pdf|xlsx?|xml|txt|csv|str|java|json|sql|sps|yxmd|htm|prpt|do|tdc|jsonld|ktr|service))$/,
    themeConfig: {
        nav: topNavMenu,
        logo: '/images/axibase_logo.png',

        sidebarDepth: 1,
        sidebar: {
            // Keep it last
            '/jobs/jdbc-data-source.html': dataSourcesMenu,
            '/jobs/kafka-consumer.html': dataSourcesMenu,
            '/jobs/http-pool.html': dataSourcesMenu,
            '/jobs/aws.html': ['/jobs/aws.html'],
            '/jobs/docker.html': ['/jobs/docker.html'],
            '/jobs/file.html': ['/jobs/file.html'],
            '/jobs/http.html': ['/jobs/http.html'],
            '/jobs/icmp.html': ['/jobs/icmp.html'],
            '/jobs/jdbc.html': ['/jobs/jdbc.html'],
            '/jobs/jmx.html': ['/jobs/jmx.html'],
            '/jobs/json.html': ['/jobs/json.html'],
            '/jobs/kafka.html': ['/jobs/kafka.html'],
            '/jobs/ovpm.html': ['/jobs/ovpm.html'],
            '/jobs/pi.html': ['/jobs/pi.html'],
            '/jobs/snmp.html': ['/jobs/snmp.html'],
            '/jobs/socrata.html': ['/jobs/socrata.html'],
            '/jobs/tcp.html': ['/jobs/tcp.html'],
            '/jobs/examples/': examplesMenu,
            '/': landingPageMenu,
            '': [],
        },

        searchMaxSuggestions: 10,

        ...githubSettings
    }
};

loadFromEnv("ga", "GA_API_KEY");
loadFromEnv("sc", "STATCOUNTER_ID");
loadFromEnv("scSec", "STATCOUNTER_SEC");

function loadFromEnv(setting, varName) {
    if (!(setting in module.exports)) {
        let value = require('process').env[varName];
        if (value) {
            module.exports[setting] = value;
        }
    }
}
