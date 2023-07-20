CREATE TABLE `Post` (
	`id`	not null	NOT NULL,
	`title`	not null	NULL,
	`content`	not null	NULL,
	`created_at`	not null	NULL,
	`updated_at`	not null	NULL,
	`user_id`	not null	NOT NULL
);

CREATE TABLE `User` (
	`id`	not null	NOT NULL,
	`name`	not null	NULL,
	`email`	not null	NULL,
	`pw`	not null	NULL,
	`created_at`	not null	NULL
);

CREATE TABLE `Comment` (
	`id`	not null	NOT NULL,
	`content`	not null	NULL,
	`created_at`	not null	NULL,
	`updated_at`	not null	NULL,
	`user_id`	not null	NOT NULL,
	`post_id`	not null	NOT NULL
);

CREATE TABLE `Hashtag` (
	`id`	not null	NOT NULL,
	`content`	not null	NULL
);

CREATE TABLE `Search` (
	`post_id`	not null	NOT NULL,
	`hashtag_id`	not null	NOT NULL
);

ALTER TABLE `Post` ADD CONSTRAINT `PK_POST` PRIMARY KEY (
	`id`
);

ALTER TABLE `User` ADD CONSTRAINT `PK_USER` PRIMARY KEY (
	`id`
);

ALTER TABLE `Comment` ADD CONSTRAINT `PK_COMMENT` PRIMARY KEY (
	`id`
);

ALTER TABLE `Hashtag` ADD CONSTRAINT `PK_HASHTAG` PRIMARY KEY (
	`id`
);

